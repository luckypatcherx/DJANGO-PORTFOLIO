from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
import random
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

from django.db import  models


def index(request):
    return HttpResponse("hello hi")

def main_home(request):
    blog_data = BlogData.objects.all()
    return render(request ,'index.html', {'blog_data': blog_data})

def userreg(request):
    return render(request,'userreg.html',{})

def contactme(request):
    if request.method == 'POST':

        vuname = request.POST.get('xname')
        vuemail = request.POST.get('xemail')
        vucontact = request.POST.get('xphno')
        vumessage=request.POST.get('xcomment')
        userdata = Userdata(Name=vuname, Email=vuemail, PhoneNo=vucontact, Message=vumessage)
        userdata.save()
        return render(request, 'index.html', {'data_submitted': True})
    else:
        return HttpResponse('Something went wrong')
def loginpanel(request):
    ud=Userdata.objects.all()
    return render(request,'admin/login.html',{'ud':ud})

def admin_login(request):
    my_data = Userdata.objects.all()
    context = {'my_data': my_data}


    al = Admindata.objects.all()
    username = request.POST.get('username')
    password = request.POST.get('password')
    for admin in al:
        # Check if username and password match
        if admin.UserId == username and admin.Password == password:
                return render(request, 'admin/leads.html', context)

    if request.GET.get('deleted') == 'True':
        return render(request, 'admin/leads.html', context)

    elif request.GET.get('portfolio') == 'True':
        return render(request,'admin/portfolio.html')

    else:
        return HttpResponse('Ayyo , Something broken')


def leads(request):
    my_data = Userdata.objects.all()
    context = {'my_data': my_data}
    return render(request, 'admin/leads.html', context)

def delete_lead(request,pk):
    my_data = Userdata.objects.all()
    context = {'my_data': my_data}
    del_data=Userdata.objects.get(pk=pk)
    del_data.delete()
    return HttpResponseRedirect('/admin_login?deleted=True')

#blog section

def blog_add(request):
    if request.method == 'POST':
        blog_title = request.POST.get('blog_title')
        blog_description = request.POST.get('blog_description')
        blog_img = request.FILES.get('blog_img')
        blog_data = BlogData(blog_title=blog_title, blog_description=blog_description, blog_img=blog_img)
        blog_data.save()
        return HttpResponse('saved success')
    else:
        return HttpResponse('Something went wrong')













# Create your views here.
