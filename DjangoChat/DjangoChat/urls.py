from django.contrib import admin
from django.urls import path, include
from django.core.asgi import get_asgi_application  # Import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter  # Import URLRouter
from channels.auth import AuthMiddlewareStack
from DjangoChat import routing  # Ensure routing is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("DjangoChat.ChitChat.urls")),  # Ensure ChitChat.urls is included
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handle HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Ensure websocket URL patterns are used
        )
    ),
})
