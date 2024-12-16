from django.views.generic import TemplateView, CreateView
from .models import GiftList, Item
from .forms import GiftListForm, ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin

class GiftList(TemplateView):
    template_name = 'giftlist/giftlist.html'

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