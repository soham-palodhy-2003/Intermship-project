"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
# from channels.http import AsgiHandler
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from onlineclasses.routing import websocket_urlpatterns
import onlineclasses.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    
    "websocket":   AuthMiddlewareStack(
        URLRouter(
            onlineclasses.routing.websocket_urlpatterns
        ),
    )
})
