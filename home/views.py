from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Event


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch event data for the countdown
        event = Event.objects.first()  # You can adjust logic to fetch a specific event
        if event:
            time_remaining = event.event_date - timezone.now()
            hours = time_remaining.seconds // 3600
            minutes = (time_remaining.seconds % 3600) // 60
            seconds = time_remaining.seconds % 60
            # Pass both the original event and countdown values
            context['event'] = event
            context['countdown'] = {
                'days': time_remaining.days,
                'hours': hours,
                'minutes': minutes,
                'seconds': seconds,
            }
        else:
            context['event'] = None
            context['countdown'] = None

        return context
