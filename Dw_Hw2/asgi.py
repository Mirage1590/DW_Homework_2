"""
ASGI config for Dw_Hw2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Hw2.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dw_Hw2.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Hw2.routing.websocket_urlpatterns
        )
    ),
})
