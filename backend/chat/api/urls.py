"""
Prepared by Backend/Server Team - Sheldon, Martin, Brian, Sarah, Veronica.
"""

from django.urls import path, re_path

from .views import ChatListView

# Register name of current Django App
app_name = 'chat'

# Register urlpaths for getting and updating chats
urlpatterns = [
    path('', ChatListView.as_view()),
]
