from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from provati.models import CustomUser
from .forms import *

#
# def admin_home(request):
#     return render(request,"picladmin/home_content.html")
#
#
# def add_staff(request):
#     return render(request,"picladmin/add_staff_template.html")


def registration_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
    context ={
        'form': form
    }
    return render(request, 'picladmin/add_staff_template.html', context)















def add_pc(request):
    return render(request,"picladmin/add_pc_template.html")

def add_monitor(request):
    return render(request,"picladmin/add_monitor_template.html")

def add_printer(request):
    return render(request,"picladmin/add_printer_template.html")


def add_ups(request):
    return render(request,"picladmin/add_ups_template.html")

def add_scanner(request):
    return render(request,"picladmin/add_scanner_template.html")

def add_switch(request):
    return render(request,"picladmin/add_switch_template.html")