from django.db import models

# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(null=False, verbose_name="Заголовок")
    content = models.CharField(null=False, verbose_name="Описание")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ["-date"]