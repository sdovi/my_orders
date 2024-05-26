from django.db import models


class Info_email(models.Model):
    title = models.CharField("Емаил  ", max_length=50)
    description = models.TextField("Коментарии", default='Нету комента',  blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Емаил"
        verbose_name_plural = "Емаил"



class Info_article(models.Model):
    title = models.CharField("Главный текст  ", max_length=50)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статья"
