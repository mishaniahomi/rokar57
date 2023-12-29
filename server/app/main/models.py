from django.db import models
import datetime


class Banner(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок баннера')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name="Изображение баннера", upload_to='banner_image/')
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    href = models.TextField(verbose_name="Ссылка", blank=True, null=True)

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'

    def __str__(self) -> str:
        return self.title
