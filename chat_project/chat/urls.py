from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),  
    path('room_list/', views.room_list, name='room_list'),
    path('<str:room_name>/', views.room, name='room'),
]