from django.urls import path
from .views import GiftList, AddGiftList

urlpatterns = [
    path('', GiftList.as_view(), name='giftlist'),
    path('add_giftlist/', AddGiftList.as_view(), name='add_giftlist'),
    path('add_item/', AddItem.as_view(), name='add_item'),
]