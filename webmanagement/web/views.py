
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
import random
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse,reverse_lazy




def index(request):
    return HttpResponse("hello hi")

def main_home(request):
    blog_data = BlogData.objects.all()
    session_variable = request.session.get('admin_id')  # retrieve session variable
    print("sessionvariable",session_variable)
    return render(request, 'index.html', {'blog_data': blog_data, 'session_variable': session_variable})
    

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

def portfolio(request):
    portfolios = PortfolioData.objects.all()
    session_variable = request.session.get('admin_id')  # retrieve session variable
    context = {'portfolios': portfolios, 'session_variable': session_variable}
    return render(request, 'portfolio.html', context)

def portfolio_app(request):
     return render(request, 'portfolio_app.html')
#resume 

def resume(request):
    return render(request,'resume.html')

#portolio






##authentication/admin


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
            # Store user ID in session
            request.session['admin_id'] = admin.id
            return render(request, 'admin/leads.html', context)
    else: 
        return render(request,'admin/login.html')


def admin_leads(request):
    # Check if user is logged in
    if 'admin_id' not in request.session:
        return redirect('admin_login')

    my_data = Userdata.objects.all()
    context = {'my_data': my_data}
    if request.GET.get('deleted') == 'True':
        return render(request, 'admin/leads.html', context)
    else:
        return render(request, 'admin/leads.html', context)

def admin_blogs(request):
    # Check if user is logged in
    if 'admin_id' not in request.session:
        return redirect('admin_login')

    return render(request, 'admin/blogs.html')

def admin_portfolio(request):
    # Check if user is logged in
    if 'admin_id' not in request.session:
        return redirect('admin_login')

    return render(request, 'admin/portfolio.html')


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

def admin_logout(request):  
    if 'admin_id' in request.session:
        del request.session['admin_id']
    return redirect(reverse('admin_login'))

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
def portfolio_add(request):
    if request.method == 'POST':
        portfolio_title = request.POST.get('portfolio_title')
        portfolio_link = request.POST.get('portfolio_link')
        portfolio_img = request.FILES.get('portfolio_img')
        portfolio_data = PortfolioData(portfolio_title=portfolio_title, portfolio_link=portfolio_link, portfolio_img=portfolio_img)
        portfolio_data.save()
        success_message = "Portfolio added successfully"
        return render(request, 'admin/portfolio.html', {'success_message': success_message})
    else:
        return render(request, 'admin/portfolio.html')
    

def delete_portfolio(request, portfolio_id):
    portfolio = PortfolioData.objects.get(id=portfolio_id)
    portfolio.delete()
    return redirect('portfolio')

def blog_delete(request, blog_id):
    blog = BlogData.objects.get(id=blog_id)
    blog.delete()
    return redirect(reverse_lazy('index') + '#blog')









