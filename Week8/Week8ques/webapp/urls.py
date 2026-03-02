from django.urls import path
from . import views

urlpatterns = [
    path('q1', views.Q1, name='home'),
    path('result/', views.result, name='result'),
    path('q2/first/', views.first_page, name='first_page'),
    path('q2/second/', views.second_page, name='second_page'),
]
