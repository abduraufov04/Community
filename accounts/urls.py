from django.urls import path
from .views import user_login, user_register, user_logout
urlpatterns = [
    path('', user_login, name = 'login'),
    path('register/', user_register, name = 'register'),
    path('logout/', user_logout, name = 'logout'),
]