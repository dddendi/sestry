from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.


def article_detail(request, title):
    article = get_object_or_404(Article, title=title)
    return render(request, 'news/news_home.html', {'art': article})



