import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'basic.settings'

import django
django.setup()

from django.conf import settings
print(f"CHANNEL_LAYERS setting: {settings.CHANNEL_LAYERS}")

from channels.layers import get_channel_layer
channel_layer = get_channel_layer()
print(f"Channel layer: {channel_layer}")