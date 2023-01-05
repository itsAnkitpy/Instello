from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('newpost/', views.NewPost, name='newpost'),
]