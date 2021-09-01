from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from history.models import History

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# @admin.action(description='Download histories XL.')
# def make_published(modeladmin, request, queryset):
#     myqs = History.objects.all()
    


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    # actions = [make_published]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# from django.contrib import admin



admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
