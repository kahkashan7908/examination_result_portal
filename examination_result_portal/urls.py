"""examination_result_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
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
from studentresultapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginPage),
    path('login',views.loginPage,name='loginPage'),
    path('signup',views.signupPage,name='signup'),
    path('main',views.mainPage,name='mainPage'),
    path('tenth',views.tenthPage,name='tenth'),
    path('inter',views.interPage,name='inter'),
    path('degree',views.degrePage,name='degree'),
    path('btech',views.btechPage,name='btech'),
    path('add1',views.addTenData),
    path('add2',views.addinterData),
    path('add3',views.adddegreeData),
    path('add4',views.adddbtechData)
]
