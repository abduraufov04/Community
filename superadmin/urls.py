from django.urls import path

from .views import AdminsListView

urlpatterns = [
    path("admin_list/", AdminsListView.as_view(), name="admin_list"),
]
