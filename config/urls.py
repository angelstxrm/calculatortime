"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.shortcuts import render
from django.conf.urls import handler404

from calculator.views import time_calculator
from tracker.views import time_tracker
    
def custom_404(request, exception):
    return render(request, 'calculator/404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('timecalculatoradmin/', admin.site.urls),
    path('', time_calculator, name='time_calculator'),
    path('time_tracker', time_tracker, name='time_tracker'),
]
