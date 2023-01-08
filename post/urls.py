from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>', views.PostDetail, name='post-details'),
    path('<uuid:post_id>/like', views.like, name='like'),
    path('<uuid:post_id>/favourite', views.favourite, name='user_favourite'),
]