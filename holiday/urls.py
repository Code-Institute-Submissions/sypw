from django.urls import path
from . import views

urlpatterns = [
    path('', views.holiday, name='holiday'),
    path('see/', views.see_holiday, name='see_holiday')
]