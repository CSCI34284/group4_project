"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica. Contributions and input from Yilin for front-end integration.
"""

from django.contrib.auth import get_user_model

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from .models import Message, Chat, Contact
from .views import get_recent_messages, get_contact_info, get_conversation

User = get_user_model()


class ChatConsumer(WebsocketConsumer):

    # Get messages on initial load
    def fetch_messages(self, data):
        messages = get_recent_messages(data['chatId'])
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.retrieve_message(content)

    # Create new message and send
    def new_message(self, data):
        contact_info = get_contact_info(data['from'])
        message = Message.objects.create(
            contact=contact_info,
            content=data['message'],
            isImage=data['isImage'])
        conversation = get_conversation(data['chatId'])
        conversation.messages.add(message)
        conversation.save()
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_new_message(content)

    """ Helper functions """
    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    # Convert multiple messages to JSON object
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    # Convert single message to JSON object
    def message_to_json(self, message):
        return {
            'id': message.id,
            'author': message.contact.user.username,
            'content': message.content,
            'isImage': message.isImage,
            'timestamp': str(message.timestamp)
        }

    # Retrieve message passed as parameter
    def retrieve_message(self, message):
        self.send(text_data=json.dumps(message))

    # Send message using Django Channels
    def send_new_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message
            }
        )

    # Send message passing an event as a parameter
    def send_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))

    """ Django Channels configuration """
    """ Resource: https://channels.readthedocs.io/en/latest/tutorial/part_3.html """
    # Connect to the current chat using Django Channels

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    # Receive data
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    # Disconnect to the current chat using Django Channels
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
