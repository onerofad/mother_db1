from django.contrib import admin
from .models import Register, MakeRequest, Support, Chats, RegisterWatcher, Cards

# Register your models here.
admin.site.register({Register, MakeRequest, Support, Chats, RegisterWatcher, Cards})
