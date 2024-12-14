from django.contrib import admin
from .models import UserMessage

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'message_type', 'timestamp')
    list_filter = ('message_type', 'timestamp')

# from django.contrib import admin
from .models import User

admin.site.register(User)
# Register your models here.
# Register your models here.
