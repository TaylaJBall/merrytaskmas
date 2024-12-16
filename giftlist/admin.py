from django.contrib import admin
from .models import GiftList, Item

# Register your models here.

@admin.register(GiftList)
class GiftListAdmin(admin.ModelAdmin):
    list_display = (
        'giftlist_id',
        'user_id',
        'person_name',
        'budget',
        'created_at',
        'updated_at',
    )
    list_filter = ('user_id',)

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'giftlist_id',
        'description',
        'link',
        'created_at',
        'updated_at',
    )
    list_filter = ('giftlist_id',)