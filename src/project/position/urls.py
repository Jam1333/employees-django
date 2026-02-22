from django.urls import path
from . import views

urlpatterns = [
    path('', views.positions, name='positions'),
    path('create/', views.create_position, name='create-position'),
    path('delete/<int:pk>', views.delete_position, name='delete-position'),
]
