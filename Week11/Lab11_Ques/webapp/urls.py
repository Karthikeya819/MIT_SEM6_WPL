from django.urls import path
from . import views

urlpatterns = [
    path('Q1/book_form', views.manage_book, name='book_form'),
    path('Q1/book_list', views.book_list, name='book_list'),
    path('Q2/', views.product_index, name='product_index'),
    path('Q2/create_product', views.create_product, name='create_product'),
    path('Q3/', views.human_management, name='human_management'),
]