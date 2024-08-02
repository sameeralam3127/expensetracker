from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('expenses/edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('expenses/delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    

]