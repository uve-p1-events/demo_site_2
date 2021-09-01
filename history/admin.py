from django.contrib import admin

# Register your models here.
from .models import History
# Register your models here.
from django.contrib.auth.admin import UserAdmin


# class HistoryAdmin(UserAdmin):
#     list_display = ('user', 'viewed_on', 'url', )
#     readonly_fields = ('viewed_on', 'url')
#     search_fields = ()
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
    

admin.site.register(History)
