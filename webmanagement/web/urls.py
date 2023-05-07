"""webmanagement URL Configuration

The `urlpatterns` list routes  to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
    
urlpatterns = [

    path('', views.main_home, name='index'),
    path('userreg/',views.userreg,name='userreg'),
    path('contactme',views.contactme,name='contactme'),
    path('login',views.loginpanel,name="login"),
    path('admin_login',views.admin_login,name='admin_login'),
    path('leads',views.leads,name='leads'),
    path('delete/<int:pk>/', views.delete_lead, name='delete_my_lead'),
    path('resume',views.resume,name="resume"),
    path('portfolio',views.portfolio,name='portfolio'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),

    ##admin urls
    
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/leads/', views.admin_leads, name='admin_leads'),
    path('admin/blogs/', views.admin_blogs, name='admin_blogs'),
    path('admin/portfolio/', views.admin_portfolio, name='admin_portfolio'),

    ##admin/add-data
    path('blogadd',views.blog_add,name="blog_add"),
    path('portadd',views.portfolio_add,name="portfolio_add"),

    ##admin/remove
    path('delete_portfolio/<int:portfolio_id>/', views.delete_portfolio, name='delete_portfolio')


























































































































































































































]
