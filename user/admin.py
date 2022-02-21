from django.contrib import admin
from .models import User
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    fields = ('name', 'phone')


admin.site.register(User, UserModelAdmin)