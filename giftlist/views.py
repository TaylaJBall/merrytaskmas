from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from giftlist.models import GiftList, Item
from .forms import GiftListForm, ItemForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class GiftLists(LoginRequiredMixin, ListView):
    template_name = "giftlist/giftlist.html"
    model = GiftList
    context_object_name = "giftlists"


class AddGiftList(LoginRequiredMixin, CreateView):
    """
    Add a Gift List
    """

    template_name = "giftlist/add_giftlist.html"
    model = GiftList
    form_class = GiftListForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddGiftList, self).form_valid(form)

    def get_success_url(self):
        return reverse("giftlist")


class DeleteGiftList(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a giftlist
    """

    model = GiftList

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse("giftlist")


class EditGiftList(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a giftlist
    """

    template_name = "giftlist/edit_giftlist.html"
    model = GiftList
    form_class = GiftListForm
    success_url = "/giftlist/"

    def test_func(self):
        return self.request.user == self.get_object().user


class Items(LoginRequiredMixin, ListView):
    template_name = "giftlist/item.html"
    model = Item
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        giftlist = GiftList.objects.get(id=self.kwargs["giftlist_id"])
        context["giftlist"] = giftlist
        context["items"] = Item.objects.filter(giftlist=giftlist)
        return context


class AddItem(LoginRequiredMixin, CreateView):
    """
    Add an Item to Gift List
    """

    template_name = "giftlist/add_item.html"
    model = Item
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giftlist"] = GiftList.objects.get(id=self.kwargs["giftlist_id"])
        return context

    def form_valid(self, form):
        giftlist = GiftList.objects.get(id=self.kwargs["giftlist_id"])
        form.instance.giftlist = giftlist
        form.instance.user = self.request.user
        return super(AddItem, self).form_valid(form)

    def get_success_url(self):
        return reverse("view_item", kwargs={"giftlist_id": self.kwargs["giftlist_id"]})


class DeleteItem(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete an Item
    """

    model = Item

    def test_func(self):
        item = self.get_object()
        return item.giftlist.user == self.request.user

    def get_success_url(self):
        giftlist_id = self.get_object().giftlist.id
        return reverse("view_item", kwargs={"giftlist_id": giftlist_id})


class EditItem(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit an Item
    """

    template_name = "giftlist/edit_item.html"
    model = Item
    form_class = ItemForm

    def test_func(self):
        return self.request.user == self.get_object().giftlist.user

    def get_success_url(self):
        giftlist_id = self.get_object().giftlist.id
        return reverse("view_item", kwargs={"giftlist_id": giftlist_id})
