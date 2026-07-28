from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='crud_list'),
    path('create/', views.item_create, name='crud_create'),
    path('update/<int:pk>/', views.item_update, name='crud_update'),
    path('delete/<int:pk>/', views.item_delete, name='crud_delete'),
]
