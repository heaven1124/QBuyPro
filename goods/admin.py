from django.contrib import admin
from .models import Goods
# Register your models here.


class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'img1', 'info')


admin.site.register(Goods, GoodsModelAdmin)