from django import forms
from .models import GiftList, Item


class GiftListForm(forms.ModelForm):
    """
    Form to create a new gift list
    """

    class Meta:
        model = GiftList
        fields = [
            "person_name",
            "budget",
        ]

        labels = {
            "person_name": "Name:",
            "budget": "Budget(£):",
        }


class ItemForm(forms.ModelForm):
    """
    Form to create new item on gift list
    """

    class Meta:
        model = Item
        fields = ["description", "link"]

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "description": "Description:",
            "link": "Link:",
        }
