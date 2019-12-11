"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica and Yilin (front-end).
"""

from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from chat.models import Chat, Contact
from chat.views import get_contact_info
from .serializers import ChatSerializer

User = get_user_model()


# Render API only when authenticated
class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_contact_info(username)
            queryset = contact.chats.all()
        return queryset
