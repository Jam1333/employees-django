from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents, name='documents'),
    path('create/', views.create_document, name='create-document'),
    path('delete/<int:pk>', views.delete_document, name='delete-document'),
]
