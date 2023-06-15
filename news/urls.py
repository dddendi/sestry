from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:title>/', views.article_detail, name='article_detail'),
]