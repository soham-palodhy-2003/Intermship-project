
import asyncio
import json
import threading
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

from onlineclasses.models import UserProfile


class StreamingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'live_stream'
        self.username = self.scope['user'].username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        message = json.loads(text_data)

        if message['type'] == 'join':
            self.username = message['username']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data,
                'username': self.username
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=event['message'])


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print(threading.get_native_id())

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        try:
            user_profile = UserProfile.objects.get(user__username=username)

            if hasattr(user_profile, 'instructor'):
                name = f'{user_profile.instructor.first_name} {user_profile.instructor.last_name}'
            elif hasattr(user_profile, 'student'):
                name = user_profile.student.name
            else:
                name = username  
        except:
            name = username  
        print("websocket:" + str(threading.get_native_id()))
        await asyncio.sleep(10)
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
