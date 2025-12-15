from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст статьи")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")

    def __str__(self):
        return self.title