from django.contrib import admin
from .models import Register, MakeRequest, Support, Chats, Payment

# Register your models here.
admin.site.register({Register, MakeRequest, Support, Chats})
