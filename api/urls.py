from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', include('users_api.urls')),
    path('messages/', include('messages_api.urls')),
    path('query/', include('query_api.urls'))
]
