# Файл url.py

from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('', views.all_quotes, name='all_quotes'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('tag/<str:tag_name>/', views.tag_detail, name='tag_detail'),
]