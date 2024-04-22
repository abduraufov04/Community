from django.urls import path
from .views import user_login, user_register, user_logout, dashboard, edit_user_to_admin, edit_admin_to_user, profile


urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('login/', user_login, name = 'login'),
    path('register/', user_register, name = 'register'),
    path('logout/', user_logout, name = 'logout'),
    path('edit_user_to_admin/', edit_user_to_admin, name = 'edit_user_to_admin'),
    path('edit_admin_to_user/', edit_admin_to_user, name = 'edit_admin_to_user'),
    path('profile/', profile, name = 'profile'),

]