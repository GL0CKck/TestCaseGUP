import geocoder
from django.db import models
from .utilites import get_timestamp_path

access_token = 'pk.eyJ1IjoiZ2xvY2tjYyIsImEiOiJja3hzdHkxM2gzNHY3Mnhxa2VwcHQ0NXo0In0.PD0hFlw0GuGQWWPfEQYy1A'


class Point(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    address = models.CharField(max_length=126, verbose_name='Адрес')
    price = models.FloatField(default=0, verbose_name='Цена')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Фото')
    descriptions = models.TextField(verbose_name='Описание')
    longitude = models.FloatField(verbose_name='Долгота', blank=True, null=True)
    latitude = models.FloatField(verbose_name='Широта', blank=True, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng
        self.latitude = g[0]
        self.longitude = g[1]
        return super(Point, self).save(*args, **kwargs)