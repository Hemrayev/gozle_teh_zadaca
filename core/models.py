from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=255, verbose_name="Url",blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = gettext("Kategoriýa")
        verbose_name_plural = gettext("Kategoriýalar")


class News(models.Model):
    source = models.URLField()
    rss_feed = models.URLField()
    title = models.CharField(max_length=500, blank=False, null=False, verbose_name=gettext("Titul"))
    slug = models.SlugField(max_length=500, unique=True, verbose_name="url")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(verbose_name=gettext("Goýlan wagty"))
    link = models.URLField(verbose_name=gettext("Web sahypasy"))
    description = models.TextField(blank=False, verbose_name=gettext("Beýany"))
    content = models.TextField(blank=False, verbose_name=gettext("Mazmuny"))
    image = models.TextField(verbose_name=gettext("Suraty"))
    thumbnail = models.TextField(verbose_name=gettext("Kiçi suraty"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def encoding_to_base64(self):
        self.image

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = gettext("Habar")
        verbose_name_plural = gettext("Habarlar")


