from django.shortcuts import render
from news.models import *
from events.models import *
from gallery.models import *
from django.http import HttpResponse


def main(request):
    articles = Article.objects.order_by('-date')[:3]
    for article in articles:
        article.first_photo = article.photos.all()[0].photo.url if article.photos.exists() \
                                                                else 'static/img/stubs/mons.jpg'
    events = Event.objects.order_by('-date')[:6]
    for event in events:
        event.first_photo = event.photos.all()[0].photo.url if event.photos.exists() \
                                                                else 'static/img/stubs/bip1.jpg'
    return render(request, 'main/main.html', {
        'articles': articles,
        'events': events,
    })


def about(request):
    return render(request, 'main/проМонастырь.html')


def masterskie(request):
    return render(request, 'main/мастерские.html')


def duhovnik(request):
    return render(request, 'main/духовник.html')


def besedyM(request):
    return render(request, 'main/беседыМатушки.html')


def besedyO(request):
    return render(request,'main/беседыОжизни.html')


def temples(request):
    return render(request, 'main/храмы.html')


def podvorie(request):
    return render(request, 'main/подворье.html')


def socprojects(request):
    return render(request,'main/соцпроекты.html')