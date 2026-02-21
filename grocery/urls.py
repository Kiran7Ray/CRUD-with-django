from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<int:id>/', views.delete_item),
    path('toggle/<int:id>/', views.toggle_complete),
]