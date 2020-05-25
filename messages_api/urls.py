from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list_messages, name='api-messages-list')
]
