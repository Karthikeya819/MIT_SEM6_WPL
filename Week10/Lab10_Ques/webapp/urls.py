from django.urls import path
from . import views

urlpatterns = [
    path('Q1', views.index, name='index'),
    path('Q1/add-category/', views.add_category, name='add_category'),
    path('Q1/add-page/', views.add_page, name='add_page'),
    path('Q2/add-work/', views.add_work, name='add_work'),
    path('Q2/search/', views.search_company, name='search_company'),
    path('A1/institutes/', views.institute_list, name='institute_list'),
]