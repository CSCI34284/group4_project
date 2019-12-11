"""
Prepared by Server Team - Sheldon, Martin, Brian, Sarah, Veronica.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('rest-auth/', include('rest_auth.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]
