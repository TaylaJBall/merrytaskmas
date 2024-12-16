from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GiftList(models.Model):
    """
    A model to create and manage giftlists
    """
    giftlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='giftlist_user', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=200)
    budget = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.person_name)

class Item(models.Model):
    """
    A model to create Items to add to giftlist
    """
    item_id = models.AutoField(primary_key=True)
    giftlist = models.ForeignKey(GiftList, related_name='giftlist', on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=False, blank=False)
    link = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.description)