from django.urls import path
from directs.views import inbox,Directs,SendMessage,UserSearch


urlpatterns = [
    path('inbox', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendMessage, name="send_message"),
    path('search/', UserSearch, name="search_users"),
    
]