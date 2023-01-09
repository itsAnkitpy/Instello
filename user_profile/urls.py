from django.urls import path

from user_profile.views import EditProfile

urlpatterns = [
    # Profile Section
    path('profile/edit', EditProfile, name="editprofile"),
]