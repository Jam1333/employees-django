from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees, name='employees'),
    path('create/', views.create_employee, name='create-employee'),
    path('delete/<int:pk>', views.delete_employee, name='delete-employee'),
]
