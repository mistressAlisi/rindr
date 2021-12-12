from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TicketForm
from django.db.models import F
from .models import Ticket
from django.core import serializers
from datetime import datetime as dt
from BI.deltaV2 import TimeCalc as _TimeCalc
import json,csv
from type.models import Type
from ticket.models import Ticket,TicketMeanTimes,TicketWeeklyResponseTimes

TimeCalc =  _TimeCalc()

def login(request):
    context = {}
    return render(request, 'login.html', context)


def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request,user)
        return JsonResponse({'res':'ok'}) 
    else:
        return JsonResponse({'res':'err'}) 
    

@login_required
def home(request):
    ticket_data = Ticket.objects.all().order_by('ticket_id')[:10]
    weekly_data = TicketWeeklyResponseTimes.objects.all()[:5]
    context = {"ticket_data":ticket_data,"weekly_data":weekly_data}
    return render(request, 'home.html', context)

@login_required
def new(request):
    form = TicketForm()
    context = {'new_ticket':form}
    return render(request, 'new.html', context)


@login_required
def new_action(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        new_ticket = form.save(commit=False)
        new_ticket.creator = request.user
        new_ticket.type.tickets += 1
        new_ticket.type.updated = dt.now()
        new_ticket.type.save()
        new_ticket.save()
        return JsonResponse({'res':'ok'}) 
    else:
        return JsonResponse({'res':'err','error':form.errors.as_json()}) 


@login_required
def table(request):
    data = Ticket.objects.filter().order_by('ticket_id')
    
    context = {"ticket_data":data}
    return render(request, 'table.html', context)

@login_required
def ticket(request,ticket):
    # data = Ticket.objects.get(id = ticket).order_by('ticket_id')
    data = Ticket.objects.get(id = ticket)
    context = {"ticket":data}
    return render(request, 'ticket.html', context)

@login_required
def ticket_export_all(request):
    data = serializers.serialize("json", Ticket.objects.filter())    
    return HttpResponse(data,content_type='application/force-download') 

@login_required
def ticket_export(request,ticket):
    type_data = serializers.serialize("json", Type.objects.filter(id= type))
    data = serializers.serialize("json", Ticket.objects.filter(id = ticket))    
    return HttpResponse(type_data+data,content_type='application/force-download') 


@login_required
def ticket_response_chart_data(request):
    data = serializers.serialize("json", TicketMeanTimes.objects.all()[:5])    
    return HttpResponse(data) 


@login_required
def ticket_weekly_chart_data(request):
    data = serializers.serialize("json", TicketWeeklyResponseTimes.objects.all()[:5])    
    return HttpResponse(data) 

#@login_required
def ticket_export_csv(request):
    tickets = Ticket.objects.filter()
    response = HttpResponse(content_type='text/csv',headers={'Content-Disposition':'attachment;filename="all_tickets.csv"'})
    writer = csv.writer(response,delimiter="\t")
    writer.writerow(['id','reference','developer','platform','difficulty','category','opened','responded','contributors','resolution','time-to-initial-resp.','core-hours','elapsed'])
    for ticket in tickets:
        delta = ticket.responded - ticket.opened
        elapsed = TimeCalc.business_lapse(ticket.opened,ticket.responded)
        if (elapsed is False):
            core_hours = False
            elapsed = "00:00:00"
        else:
            core_hours=  True
        writer.writerow([ticket.id,ticket.reference,ticket.affirmer,ticket.get_system_display(),ticket.difficulty,ticket.type.label,ticket.opened,ticket.responded,ticket.contributors,ticket.notes,delta,core_hours,elapsed])
        ticket.exported = True

    return response
