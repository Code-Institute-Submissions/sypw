from django.urls import path
from . import views
# from comunicado.views import addInDiscussion, addInForum


urlpatterns = [
    path('', views.comunicado, name='comunicado'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('edit/<int:forum_id>/', views.editInForum, name='editInForum'),
    path('edit/1/<int:discussion_id>/', views.editInDiscussion, name='editInDiscussion'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]
