from django.urls import path
from . import views

urlpatterns = [
    path('', views.firewall_list_view, name='firewall_list_view'),
]
