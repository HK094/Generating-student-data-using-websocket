import os
import django
from channels.layers import get_channel_layer
from channels_redis.core import RedisChannelLayer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic.settings')
django.setup()

print("Imports successful")
print(f"RedisChannelLayer: {RedisChannelLayer}")

from django.conf import settings
print(f"CHANNEL_LAYERS setting: {settings.CHANNEL_LAYERS}")

channel_layer = get_channel_layer()
print(f"Channel layer: {channel_layer}")