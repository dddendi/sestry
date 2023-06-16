from django.db import models
from datetime import datetime
# Create your models here.


class Photo(models.Model):
    image = models.ImageField('Картинка', upload_to=f'static/img/news/%Y%m%d%H%M%S', default='mons.jpg')
    alt = models.CharField('Альт. текст', max_length=50)
    date = models.DateTimeField('Дата публикации', default=datetime.now)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фотография'
        ordering = ['date']
