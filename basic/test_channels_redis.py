import os
import django
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic.settings')
django.setup()

channel_layer = get_channel_layer()
print(f"Channel layer: {channel_layer}")

try:
    async_to_sync(channel_layer.group_add)("test_group", "test_channel")
    print("Successfully added to group")
    async_to_sync(channel_layer.group_send)("test_group", {"type": "test.message", "text": "Hello there!"})
    print("Successfully sent message to group")
except Exception as e:
    print(f"An error occurred: {e}")

print("Test completed.")