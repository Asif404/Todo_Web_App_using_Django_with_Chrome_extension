"""Todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from polls import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import  views as auth_views
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('polls/', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path('api/post_form/', views.post_form_api, name="post_form_api"),
    path('api/del_task',views.del_task,name="del_task"),
    path('api/del_titile',views.del_titile,name="del_titile"),
]
