from django.urls import path
from blogapp import views

urlpatterns = [
    path('about',views.aboutpage),
    path('test',views.testpage),
    path('contact',views.contactpage),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    # path('home/<x>/<y>',views.homepage),
    path('hello',views.helloview),
    path('',views.homepage),
    path('userdashboard',views.user_dashboard),
    path('createblog',views.create_blog),
    path('see_det/<rid>',views.view_details),
    path('publish/<status>/<rid>',views.is_published),
    path('setcookies',views.setcookies),
    path('getcookies',views.getcookies),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('dform',views.djangoForm),
    # path('dform',views.djangoForm),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
]