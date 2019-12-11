"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica. Scheme created by Sarah.
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Contact table structure
class Contact(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


# Message table structure
class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    isImage = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


# Chat table structure
class Chat(models.Model):
    participants = models.ManyToManyField(Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return "{}".format(self.pk)
