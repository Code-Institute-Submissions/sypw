from django.urls import path
from . import views
# from comunicado.views import addInDiscussion, addInForum


urlpatterns = [
    path('', views.comunicado, name='comunicado'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]
