from django.views.generic import TemplateView

class GiftList(TemplateView):
    template_name = 'giftlist/giftlist.html'