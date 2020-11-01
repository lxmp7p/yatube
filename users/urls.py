from django.contrib.auth import views
from django.urls import path
from . import views as form
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', form.registration, name='registration'),
]