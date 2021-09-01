from django.urls import path

from . import views

urlpatterns = [
    path("",views.help_desk.as_view(),name="help_desk"),
    
]

ajax_urls = [
    # path('chat', views.chat, name='chatwindow'),
    path('getChatUserInfo', views.getChatUserInfo, name='getChatUserInfo'),
    path('log_message', views.log_message, name='logMessage'),
    path('getChats', views.get_all_chats, name='getChats'),
    path('loadmessages', views.load_previous_messages, name='loadPreviousMessages'),
]

urlpatterns = urlpatterns + ajax_urls
