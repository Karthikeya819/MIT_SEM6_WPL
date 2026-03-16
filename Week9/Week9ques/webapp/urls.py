from django.urls import path, include
from . import views

urlpatterns = [
    path('q1/', views.q1, name='Q1'),
    path('q2/', views.q2, name='Q2'),
    path('q3/', views.q3p1, name='Q3'),
    path('q3_result/', views.q3p2, name='Q3_Result'),
    path('a1/', views.a1, name='A1'),
    path('a2/', views.a2, name='A2'),
]