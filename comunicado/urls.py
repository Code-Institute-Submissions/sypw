from django.urls import path
from . import views
# from comunicado.views import addInDiscussion, addInForum


urlpatterns = [
    path('', views.comunicado, name='comunicado'),
    path('add_in_forum/', views.add_in_forum, name='add_in_forum'),
    path('add_in_discussion/<int:forum_id>/', views.add_in_discussion, name='add_in_discussion'),
    # path('edit/<int:forum_id>/', views.edit_in_forum, name='edit_in_forum'),
    path('disc/edit/<int:discussion_id>/', views.edit_in_discussion, name='edit_in_discussion'),
    path('delete/<int:forum_id>/', views.delete_in_forum, name='delete_in_forum'),
    path('disc/delete/<int:discussion_id>/', views.delete_in_discussion, name='delete_in_discussion'),
]
