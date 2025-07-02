from django.urls import path
from . import views

urlpatterns = [
    path('criar_post/', views.criar_post, name='criar_post'),
    path('criar_autor/', views.criar_autor, name='criar_autor'),
    path('criar_categoria/', views.criar_categoria, name='criar_categoria'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
