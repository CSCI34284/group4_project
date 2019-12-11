"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica and Yilin (front-end).
"""

from rest_framework import serializers

from chat.models import Chat, Contact
from chat.views import get_contact_info


# Serialize contact data
class ContactSerializer(serializers.StringRelatedField):

    # Restore to python primitive
    def to_internal_value(self, value):
        return value


# Serialize chat data
class ChatSerializer(serializers.ModelSerializer):

    # Serialize participant data with many-to-many relationships
    participants = ContactSerializer(many=True)

    # Assign model and fields
    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')
        read_only = ('id')

    # Create/save chat data and participants
    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        for username in participants:
            contact = get_contact_info(username)
            chat.participants.add(contact)
        chat.save()
        return chat
