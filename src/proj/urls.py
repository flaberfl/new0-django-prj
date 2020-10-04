from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('service_detail/', views.service_detail, name='service_detail'),
    path('service_list/', views.service_list, name='service_list'),
]
