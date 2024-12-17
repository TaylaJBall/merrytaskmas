from django.urls import path
from .views import (
    GiftLists, Items, AddGiftList,
    AddItem, DeleteGiftList, DeleteItem,
    EditGiftList, EditItem
)

urlpatterns = [
    path('', GiftLists.as_view(), name='giftlist'),
    path('add_giftlist/', AddGiftList.as_view(), name='add_giftlist'),
    path('giftlist/<int:giftlist_id>/add_item/', AddItem.as_view(), name='add_item'),
    path("giftlist/<int:giftlist_id>/view_item/", Items.as_view(), name="view_item"),
    path("delete/giftlist/<int:pk>/", DeleteGiftList.as_view(), name="delete_giftlist"),
    path("delete/item/<int:pk>/", DeleteItem.as_view(), name="delete_item"),
    path("edit/giftlist/<int:pk>/", EditGiftList.as_view(), name="edit_giftlist"),
    path("edit/item/<int:pk>/", EditItem.as_view(), name="edit_item"),
]