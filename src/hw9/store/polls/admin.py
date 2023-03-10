from django.contrib import admin
from .models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase



class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'name')

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'picture')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'registered_at')

class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'registered_at')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'owner')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price')

class MyBugAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'total_price')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'buy_time')


admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MyBug, MyBugAdmin)
admin.site.register(Purchase, PurchaseAdmin)