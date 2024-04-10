

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('get_bot_response/', views.get_bot_response, name='get_bot_response'),
]
