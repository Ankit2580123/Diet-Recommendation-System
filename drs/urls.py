"""drs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from home.views import*

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('signup',signup,name='signup'),
    path('contact/',contact,name='contact'),
    path('userlist/',user_list,name='userlist'),
    path('home/',home,name='home'),
    path('bmi/',bmi,name='bmi'),
    path('logout/',handleLogout,name="logout"),
    path('del_user/<id>',delete_user,name='delete_user'),
    
    path('dietform/',dietform,name='dietform'),
    path('editUser/<id>',editUser,name="editUser"),
    path('updateUser/',update_user,name='update_user'),
    path('recommendation/',recommendation,name='recommendation'),
    path('admin/', admin.site.urls),
]
