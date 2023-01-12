from django.urls import path
from directs.views import inbox

urlpatterns = [
    path('inbox', inbox, name="message"),
    
]