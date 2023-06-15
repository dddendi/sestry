from django.shortcuts import render, get_object_or_404
from .models import Event
# Create your views here.


def event_detail(request, title):
    event = get_object_or_404(Event, title=title)
    return render(request, 'events_home.html', {'ev': event})



