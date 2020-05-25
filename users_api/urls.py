from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list_users, name='api-users-list')
]
