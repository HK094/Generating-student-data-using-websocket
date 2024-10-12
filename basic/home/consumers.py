from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncWebsocketConsumer
class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        self.channel_layer = get_channel_layer()
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,  
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from django channels'}))

    def receive(self, text_data):
        print(f"Received message: {text_data}")
        self.send(text_data=json.dumps({'status': 'received from django channels'}))
        # You can add more logic here to handle incoming messages

    def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        ) 

    def send_notification(self, event):
        print(f"Sending notification: {event}")
        print(event['value'])
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))

class NewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        await (self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({'status':'connected from new async consumer'}))

    async def receive(self, text_data):
        print(f"Received message: {text_data}")
        self.send(text_data=json.dumps({'status': 'WE GOT U'}))

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")                                                       
        await (self.channel_layer.group_discard)(self.room_group_name, self.channel_name)
    
    async def send_student_data(self, event):
        print(f"Sending notification: {event}")
        print(event['value'])
        data = json.loads(event.get('value'))
        await  self.send(text_data=json.dumps({'payload': data})) 