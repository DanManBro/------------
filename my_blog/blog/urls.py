from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('new/', views.article_create, name='article_create'),
    path('edit/<int:pk>/', views.article_update, name='article_update'),
    path('delete/<int:pk>/', views.article_delete, name='article_delete'),
]