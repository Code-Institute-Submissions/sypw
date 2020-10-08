from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('decide/', views.decide, name='decide'),
]
