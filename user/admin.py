from django.contrib import admin
from .models import UserModel
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    fields = ('name', 'auth_key', 'phone')


admin.site.register(UserModel, UserModelAdmin)