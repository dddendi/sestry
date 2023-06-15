from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='Главная'),
    path('О монастыре/', views.about, name='О монастыре'),
    path('Мастерские/', views.masterskie, name='Мастерские'),
    path('Слово духовника/', views.duhovnik, name='Слово духовника'),
    path('Беседы матушки/', views.besedyM, name='Беседы матушки'),
    path('Храмы/', views.temples, name="Храмы"),
    path('Подворье в меркушино/', views.podvorie, name='Подворье'),
    path('Служение ближним/',views.socprojects,name='Соцпроекты'),
    path('Беседы о жизни',views.besedyO,name='Беседы о жизни'),
]
