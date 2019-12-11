"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica, Yilin. Based on Scheme prepared by Sarah and required API calls.
"""

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact

User = get_user_model()


# Get messages and order oldest to newest
def get_recent_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:100]


# Get the current Contact
def get_contact_info(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


# Get the current Chat ID
def get_conversation(chatId):
    return get_object_or_404(Chat, id=chatId)
