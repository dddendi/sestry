from django.db import models
from datetime import datetime
# Create your models here.


class Event(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Текст события')
    date = models.DateTimeField('Дата публикации', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'События'
        verbose_name = 'Событие'
        ordering = ['date']


class ShowPhoto(models.Model):
    show = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to=f'static/img/events/%Y%m%d%H%M%S')
