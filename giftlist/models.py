from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GiftList(models.Model):
    """
    A model to create and manage giftlists
    """
    giftlistID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, related_name='giftlist_user', on_delete=models.CASCADE)
    