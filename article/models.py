from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    content = models.TextField(verbose_name='текст статьи')
    photo = models.ImageField(verbose_name='фото',blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=False)
    is_daily = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title