from django.contrib.auth import get_user_model
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message

User = get_user_model()




group_n_chats = {}

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        room = data['room']
        messages = Message.last_all_messages(room=room)
        print('messages',messages)
        content = {
            'messages': self.messages_to_json(messages),
            "command": "fetch_messages"
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['from']
        room = data['room']
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(
            author=author_user, content=data['message'],room=room)
        content = {
            'command':'new_message',
            'messages':self.messages_to_json([message]),
        }
        # print(self.message_to_json(message))
        
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = "helpgroup"
        self.room_group_name = 'chat_%s_%s' % (self.room_name,self.group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        # print("data",data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'messages': message,
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['messages']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'messages': message,
        }))
