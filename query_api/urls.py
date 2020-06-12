from django.urls import path, include
from . import views

# URLs used to access query functions of the app
urlpatterns = [
    path('users/', views.list_users, name='api-users-list'),
    path('chats/', views.list_chats, name='api-chats-list'),
    path('lists/', views.list_lists, name='api-lists-list')
]