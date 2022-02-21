from django.contrib import admin
from .models import Active, ActiveGoods

# Register your models here.


class ActiveModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img1', 'start_time', 'end_time')


class ActiveGoodsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'goods', 'rate')


admin.site.register(Active, ActiveModelAdmin)
admin.site.register(ActiveGoods, ActiveGoodsModelAdmin)