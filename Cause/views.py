from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from .forms import CauseForm
from .models import Cause
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from ticket.models import Ticket

# Create your views here.


@login_required
def new(request):
    form = CauseForm()
    context = {'new_cause':form}
    return render(request, 'new_cause.html', context)


@login_required
def new_action(request):
    form = CauseForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'res':'ok'})
    else:
        print(form.errors)

        return JsonResponse({'res':'err','error':'err'})


@login_required
def table(request):
    data = Cause.objects.filter()

    context = {"cause_data":data}
    return render(request, 'cause_table.html', context)


@login_required
def cause(request, cause):
    data = Cause.objects.get(id = cause)
    tickets = Ticket.objects.filter(cause_id= data).order_by('ticket_id')[:10]
    context = {"cause":data,"ticket_data":tickets}
    return render(request, 'cause.html', context)

@login_required
def cause_export(request,cause):
    cause_data = serializers.serialize("json", Cause.objects.filter(id= cause))
    data = serializers.serialize("json", Ticket.objects.filter(cause_id= cause))
    return HttpResponse(cause_data+","+data,content_type='application/force-download')

@login_required
def cause_export_all(request):
    cause_data = serializers.serialize("json", Cause.objects.filter())
    return HttpResponse(cause_data,content_type='application/force-download')

@login_required
def cause_chart_data(request):
    data = serializers.serialize("json", Cause.objects.all().order_by('tickets')[:5])
    return HttpResponse(data)

@login_required
def cause_time_chart_data(request):
    data = serializers.serialize("json", Cause.objects.all().order_by('tickets')[:5])
    return HttpResponse(data)
