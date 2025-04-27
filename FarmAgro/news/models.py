from django.urls import reverse
from django.db import models
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    #CharField просто должен быть небольшой текст # max_legth - максимальное кол-во символов # Verbose_name-имя которое будет указаано вместо titile
    content = models.TextField(blank=True, verbose_name='Контент')
    #TextField - Текстовое поле предназначеное для большого текста#blank - поле может быть пустым#null- поле не может быть пустым и зстандартное значение NULL
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    #DateTimeField - дата создания новости # auto_now_add - Когда добавляеться
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    #auto_now - Когда обновлялось
    photo = models.ImageField(upload_to='News', verbose_name='Прикрепить файл', blank=True,max_length=100)
    #ImageField - Изображение #upload_to - Когда добвили
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    #BooleanField  - галочка # default - исползуеться для обозначения условий - опублковано или нет
    category = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name='Категория', related_name='get_news')
    #ForeignKey - Поля отношений
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse(viewname='view_news', kwargs={"pk": self.pk})




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        # Название новости
        verbose_name_plural = 'Новости'
        #Список новостей
        ordering = ['-created_at']
        #Порядок новостей


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Имя Категории')
    #Под класс Meta
    def get_absolute_url(self):
        return  reverse(viewname='category', kwargs={"category_id": self.pk})






    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']















