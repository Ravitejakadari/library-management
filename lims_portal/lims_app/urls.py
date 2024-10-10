from django.contrib import admin
from django.urls import path
from .views import *  
from .import views  

urlpatterns = [
    path('', home),
    path('home', home),
    path('readers', readers_tab),
    path('save', save_student),
    path('readers/add', save_reader),
    path('register/', views.registerPage, name="register"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('books', books),
    path('index/', views.index_view, name='index'),
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:pk>/', views.update_book, name='update_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book')
]