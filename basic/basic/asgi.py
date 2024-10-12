import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from home.consumers import TestConsumer, NewConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/test/', TestConsumer.as_asgi()),
            path('ws/new/', NewConsumer.as_asgi()),
        ])
    ),
})