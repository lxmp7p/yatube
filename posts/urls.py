from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addPost/<str:slug>/', views.add_post, name='add_post'),
    path('groupsList/', views.watch_group_list, name='watch_group_list'),
    path('groups/<str:slug>/', views.watch_group, name='watch_group'),
]