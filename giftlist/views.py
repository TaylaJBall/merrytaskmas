from django.views.generic import TemplateView, CreateView
from .models import GiftList
from .forms import GiftListForm, ItemForm

class GiftList(TemplateView):
    template_name = 'giftlist/giftlist.html'

class AddGiftList(CreateView):
    """
    Add Giftlist
    """
    template_name = 'giftlist/add_giftlist.html'
    model = GiftList
    form_class = GiftListForm
    success_url = 'giftlist/giftlist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddGiftList, self).form_valid(form)

