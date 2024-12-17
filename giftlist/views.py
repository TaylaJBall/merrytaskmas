from django.views.generic import CreateView, ListView, DetailView
from giftlist.models import GiftList, Item
from .forms import GiftListForm, ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin

class GiftLists(ListView):
    template_name = 'giftlist/giftlist.html'
    model = GiftList
    context_object_name = 'giftlists'

class AddGiftList(LoginRequiredMixin ,CreateView):
    """
    Add a Gift List
    """
    template_name = 'giftlist/add_giftlist.html'
    model = GiftList
    form_class = GiftListForm
    success_url = 'giftlist/giftlist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddGiftList, self).form_valid(form)


class Items(DetailView):
    template_name = 'giftlist/item.html'
    model = Item
    context_object_name = 'item'


class AddItem(LoginRequiredMixin, CreateView):
    """
    Add an Item to Gift List
    """
    template_name = 'giftlist/add_item.html'
    model = Item
    form_class = ItemForm
    success_url = 'giftlist/giftlist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddItem, self).form_valid(form)