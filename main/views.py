from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/проМонастырь.html')


def masterskie(request):
    return render(request, 'main/мастерские.html')


def duhovnik(request):
    return render(request, 'main/духовник.html')


def besedyM(request):
    return render(request, 'main/беседыМатушки.html')


def temples(request):
    return render(request, 'main/храмы.html')


def podvorie(request):
    return render(request, 'main/подворье.html')

def socprojects(request):
    return render(request,'main/соцпроекты.html')