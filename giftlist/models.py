from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class GiftList(models.Model):
    """
    A model to create and manage giftlists
    """

    user = models.ForeignKey(
        User, related_name="giftlist_user", on_delete=models.CASCADE
    )
    person_name = models.CharField(max_length=200, default=None)
    budget = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.person_name)


class Item(models.Model):
    """
    A model to create Items to add to giftlist
    """

    giftlist = models.ForeignKey(
        GiftList, related_name="giftlist", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=500, null=False, blank=False)
    link = models.URLField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.description)
