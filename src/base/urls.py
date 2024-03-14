from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]
