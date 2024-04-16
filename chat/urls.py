from django.urls import path
from .views import chat, your_view, get_chat_list, get_history, get_history_js

urlpatterns = [
    path('', chat, name = "chat"),
    path('send/', your_view, name = "ajax_example"),
    path('get_chat_list/', get_chat_list, name = 'get_chat_list'),
    path('get_history/<int:pk>/', get_history, name = 'get_history'),
    path('get_history_js/<int:pk>/', get_history_js, name = 'get_history_js'),
    
]
