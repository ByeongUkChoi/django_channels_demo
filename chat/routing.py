from channels.routing import route
from chat.consumers import ws_connect, ws_receive, ws_disconnect
from django.conf.urls import include

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect),
]