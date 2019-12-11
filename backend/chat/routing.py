"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica.
"""

from django.urls import re_path
from .consumers import ChatConsumer

# Assign pattern to activate selected websocket
websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]
