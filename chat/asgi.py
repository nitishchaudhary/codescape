import os
import chat.routing
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
# from channels.routing import get_default_application
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Codeshare.settings')

application = ProtocolTypeRouter({
     'http': get_asgi_application(),
     'websocket':AuthMiddlewareStack(
          URLRouter(
               chat.routing.websocket_urlpatterns
          )
     )
})

