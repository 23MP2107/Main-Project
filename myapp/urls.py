"""project URL Configuration

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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('webcam_test', views.webcam_test, name='webcam_test'),


    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_type_master_add', views.admin_type_master_add, name='admin_type_master_add'),
    path('admin_type_master_edit', views.admin_type_master_edit, name='admin_type_master_edit'),
    path('admin_type_master_view', views.admin_type_master_view, name='admin_type_master_view'),
    path('admin_type_master_delete', views.admin_type_master_delete, name='admin_type_master_delete'),

    path('admin_data_set_add', views.admin_data_set_add, name='admin_data_set_add'),
    path('admin_data_set_view', views.admin_data_set_view, name='admin_data_set_view'),
    path('admin_data_set_delete', views.admin_data_set_delete, name='admin_data_set_delete'),

    path('admin_question_pool_add', views.admin_question_pool_add, name='admin_question_pool_add'),
    path('admin_question_pool_view', views.admin_question_pool_view, name='admin_question_pool_view'),
    path('admin_question_pool_delete', views.admin_question_pool_delete, name='admin_question_pool_delete'),

    path('admin_user_view', views.admin_user_view, name='admin_user_view'),
    path('admin_user_details_add', views.admin_user_details_add, name='admin_user_details_add'),
    path('admin_user_delete', views.admin_user_delete, name='admin_user_delete'),



    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_user_exam1_view', views.user_user_exam1_view, name='user_user_exam1_view'),
    path('user_user_exam1_add', views.user_user_exam1_add, name='user_user_exam1_add'),

    path('user_user_exam2_view', views.user_user_exam2_view, name='user_user_exam2_view'),
    path('user_user_exam2_add', views.user_user_exam2_add, name='user_user_exam2_add'),

    path('user_webcam_test', views.user_webcam_test,name='user_webcam_test'),

]
