"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica.
"""

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# Websocket integration and URL designation
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
