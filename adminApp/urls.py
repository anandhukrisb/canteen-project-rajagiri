from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_page, name='admin-page'),
    path('order/<uuid:token>/', views.place_order, name='place_order'),
]
