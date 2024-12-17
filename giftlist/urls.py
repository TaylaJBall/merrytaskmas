from django.urls import path
from .views import GiftLists, Items, AddGiftList, AddItem

urlpatterns = [
    path('', GiftLists.as_view(), name='giftlist'),
    path('add_giftlist/', AddGiftList.as_view(), name='add_giftlist'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path("<int:pk>/", Items.as_view(), name="view_item"),
]