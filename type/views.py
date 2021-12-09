from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from .forms import TypeForm
from .models import Type
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from ticket.models import Ticket

# Create your views here.


@login_required
def new(request):
    form = TypeForm()
    context = {'new_type':form}
    return render(request, 'new_type.html', context)


@login_required
def new_action(request):
    form = TypeForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'res':'ok'}) 
    else:
        print(form.errors)
        
        return JsonResponse({'res':'err','error':'err'}) 


@login_required
def table(request):
    data = Type.objects.filter()
    
    context = {"type_data":data}
    return render(request, 'type_table.html', context)


@login_required
def type(request,type):
    data = Type.objects.get(id = type)
    tickets = Ticket.objects.filter(type_id= data).order_by('ticket_id')[:10]
    context = {"type":data,"ticket_data":tickets}
    return render(request, 'type.html', context)

@login_required
def type_export(request,type):
    type_data = serializers.serialize("json", Type.objects.filter(id= type))
    data = serializers.serialize("json", Ticket.objects.filter(type_id= type))
    return HttpResponse(type_data+","+data,content_type='application/force-download') 

@login_required
def type_export_all(request):
    type_data = serializers.serialize("json", Type.objects.filter())
    return HttpResponse(type_data,content_type='application/force-download') 

@login_required
def type_chart_data(request):
    data = serializers.serialize("json", Type.objects.all().order_by('tickets')[:5])    
    return HttpResponse(data) 

@login_required
def type_time_chart_data(request):
    data = serializers.serialize("json", Type.objects.all().order_by('tickets')[:5])    
    return HttpResponse(data)     
