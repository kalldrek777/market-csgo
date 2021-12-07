from django.db import models
import datetime


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название продукта')
    text = models.TextField(max_length=200, unique=True, verbose_name='Описание продукта')
    img = models.ImageField(unique=False, verbose_name='Изображение продукта', upload_to='images/')
    category = models.CharField(max_length=20, unique=False,  verbose_name='Категория продукта')
    date = models.DateTimeField(verbose_name='дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
