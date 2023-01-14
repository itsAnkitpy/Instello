from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from user_profile.views import Profile
from user_profile.views import UserProfile,follow


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('users/', include('user_profile.urls')),
    path('message/', include('directs.urls')),
    
    # Profile URL section
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved/', UserProfile, name='favourite'),
    path('<username>/follow/<option>/', follow, name='follow'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
