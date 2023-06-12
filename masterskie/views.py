from django.shortcuts import render

# Create your views here.


def masterskie(request):
    return render(request, 'main/мастерские.html')


def ikonopisnaya(request):
    return render(request, 'main/иконописное.html')


def shveinaya(request):
    return render(request, 'main/швейное.html')


def izdat(request):
    return render(request, 'main/издательство.html')


def hor(request):
    return render(request, 'main/хор.html')


def prosfornya(request):
    return render(request, 'main/просфорня.html')