"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica.
"""

from django.contrib import admin

from .models import Contact, Chat, Message

# Register models (database tables) for viewing in Django Admin UI
admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)
