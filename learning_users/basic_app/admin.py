from django.contrib import admin
from basic_app.models import UserProfileInfo
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'portfolio_site', 'profile_pic')


admin.site.register(UserProfileInfo, UserAdmin)
