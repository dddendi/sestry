from django.db import models
from datetime import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons_icon = models.ImageField('Анонс-фото', upload_to='static/img/news')
    anons_text = models.CharField('Анонс-текст', max_length=400)
    full_text = models.TextField('Текст новости')
    images = models.ImageField('Фото к новости', upload_to='static/img/news')
    date = models.DateTimeField('Дата публикации',default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
