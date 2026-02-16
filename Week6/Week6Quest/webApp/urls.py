from django.urls import path, include
from . import views

urlpatterns = [
    path('Q1', views.Q1),
    path('Q2', views.Q2),
    path('Q3', views.home, name='home'),
    path('Q3/metadata/', views.metadata, name='metadata'),
    path('Q3/reviews/', views.reviews, name='reviews'),
    path('Q3/publisher/', views.publisher, name='publisher'),
    path("A1/", views.A1, name="good"),

]
