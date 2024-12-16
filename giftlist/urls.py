from django.urls import path
from .views import GiftList

urlpatterns = [
    path('', GiftList.as_view(), name='giftlist')
]