"""ictproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ictproject2 import settings
from provati import views, provatiadminViews, provatiserviceViews

urlpatterns = [
    path('demo',views.showDemo),
    path('admin/', admin.site.urls),
    path('',views.showlogin),
    path('home_content',views.homepage),


    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user),
    path('doLogin',views.doLogin),
    # path('admin_home',provatiadminViews.admin_home),
    path('register/', provatiadminViews.registration_view, name='register'),
    path('add_pc',provatiadminViews.add_pc),
    path('add_monitor',provatiadminViews.add_monitor),
    path('add_printer',provatiadminViews.add_printer),
    path('add_ups',provatiadminViews.add_ups),
    path('add_scanner',provatiadminViews.add_scanner),
    path('add_switch',provatiadminViews.add_switch),




    path('picl_service',provatiserviceViews.picl_service),
    path('picl_service_bill',provatiserviceViews.picl_service_bill),
    path('picl_product_bill',provatiserviceViews.picl_product_bill),


    # save new url for insert data Here
    # path('add_staff_save',provatiadminViews.add_staff_save),



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
