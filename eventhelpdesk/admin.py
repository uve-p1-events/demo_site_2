from django.contrib import admin
from .models import Messages, UserStatus

# for ajac-chat
# Register your models here.
admin.site.register(Messages)

class messagesTable(admin.ModelAdmin):
    list_display = ('id', 'text', 'owner', 'timestamp', 'recipient', 'isGroup', 'groupId', 'approval_status')
    # list_display = ('id', 'owner')

class userStatusTable(admin.ModelAdmin):
    list_display = ('id', 'owner', 'reader', 'onGroup', 'groupId', 'typing_status', 'timestamp')


admin.site.unregister(Messages)
admin.site.register(Messages, messagesTable)
admin.site.register(UserStatus, userStatusTable)
