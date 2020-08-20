from django.urls import path
from home import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('login_customer', views.login_customer),
    path('view_details', views.view_details)
]