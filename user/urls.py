from django.urls import path
from .views import view_user

urlpatterns = [
    path('',view_user),
]
