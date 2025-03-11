"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})