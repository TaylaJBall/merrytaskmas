from django.contrib import admin
from .models import GiftList, Item

# Register your models here.

@admin.register(GiftList)
class GiftListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'person_name',
        'budget',
        'created_at',
        'updated_at',
    )
    list_filter = ('user',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'giftlist',
        'description',
        'link',
        'created_at',
        'updated_at',
    )
    list_filter = ('giftlist',)