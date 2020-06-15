from django.urls import path, include
from . import views

# URLs used to access query functions of the app
urlpatterns = [
    path('users/', views.query_users, name='api-query-users'),
    path('chats/', views.query_chats, name='api-query-chats'),
    path('lists/', views.query_lists, name='api-query-lists')
]
