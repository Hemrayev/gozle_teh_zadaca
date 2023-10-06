from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategoriýa"
        verbose_name_plural = "Kategoriýalar"


class Source(models.Model):
    name = models.URLField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Sslyka"
        verbose_name_plural = "Ssylkalar"


class Rss(models.Model):
    name = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Rsslar"


class News(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    rss_feed = models.ForeignKey(Rss, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=False, null=False, verbose_name="Titul")
    pub_date = models.DateTimeField(verbose_name="Goýlan wagty")
    link = models.URLField(verbose_name="Web sahypasy")
    description = models.TextField(blank=False, verbose_name="Beýany")
    content = models.TextField(blank=False, verbose_name="Mazmuny")
    image = models.TextField(verbose_name="Suraty", blank=False)
    thumbnail = models.TextField(verbose_name="Kiçi suraty", blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Habar"
        verbose_name_plural = "Habarlar"


