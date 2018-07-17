from django.contrib import admin
from .models import AddGoods, Clerk, Counter


# Register your models here.
class AddGoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'created_time', 'clerk', 'counter']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10


class ClerkAdmin(admin.ModelAdmin):
    list_display = ['name', 'join_time', 'is_available']
    search_fields = ['name']
    list_filter = ['join_time']
    list_per_page = 10


class CounterAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'address', 'clerk']
    search_fields = ['address']
    list_filter = ['clerk']
    list_per_page = 10


admin.site.register(AddGoods, AddGoodsAdmin)
admin.site.register(Clerk, ClerkAdmin)
admin.site.register(Counter, CounterAdmin)
