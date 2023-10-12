from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext


class CategoryTk(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategoriýa_Tk"
        verbose_name_plural = "Kategoriýalar_Tk"


class CategoryEn(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategoriýa_En"
        verbose_name_plural = "Kategoriýalar_En"


class CategoryRu(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Kategoriýa_Ru"
        verbose_name_plural = "Kategoriýalar_Ru"


class Rss(models.Model):
    name = models.URLField(verbose_name="Rss_sahypasy")
    source = models.URLField(verbose_name="haysy_sayt")
    logo = models.TextField(verbose_name='Logotipi')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Rsslar"


class News(models.Model):
    rss_feed = models.ForeignKey(Rss, on_delete=models.CASCADE, blank=True, null=True)
    source = models.URLField()
    category_tk = models.ManyToManyField(CategoryTk, blank=True)
    title = models.CharField(max_length=500, blank=False, null=False, verbose_name="Titul")
    slug = models.SlugField(max_length=255, verbose_name='Api_urly', unique=True)
    pub_date = models.DateTimeField(verbose_name="Goýlan wagty")
    link = models.URLField(verbose_name="Web sahypasy")
    content = models.TextField(blank=False, verbose_name="Mazmuny")
    image = models.TextField(verbose_name="Suraty", blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Habar"
        verbose_name_plural = "Habarlar"


class NewsEnglish(models.Model):
    rss_feed = models.ForeignKey(Rss, on_delete=models.CASCADE, blank=True)
    source = models.URLField()
    category_en = models.ManyToManyField(CategoryEn, blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Api_urly')
    title = models.CharField(max_length=500, blank=False, null=False, verbose_name="Titul")
    pub_date = models.DateTimeField(verbose_name="Goýlan wagty")
    link = models.URLField(verbose_name="Web sahypasy")
    content = models.TextField(blank=False, verbose_name="Mazmuny")
    image = models.TextField(verbose_name="Suraty", blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Habar_Inlis"
        verbose_name_plural = "Habarlar_Inlis"


class NewsRussian(models.Model):
    rss_feed = models.ForeignKey(Rss, on_delete=models.CASCADE, blank=True, null=True)
    source = models.URLField()
    category_ru = models.ManyToManyField(CategoryRu, blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Api_urly')
    title = models.CharField(max_length=500, blank=False, null=False, verbose_name="Titul")
    pub_date = models.DateTimeField(verbose_name="Goýlan wagty")
    link = models.URLField(verbose_name="Web sahypasy")
    content = models.TextField(blank=False, verbose_name="Mazmuny")
    image = models.TextField(verbose_name="Suraty", blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Habar_Rus"
        verbose_name_plural = "Habarlar_Rus"



