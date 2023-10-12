from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_filter = ['source', 'category_tk', 'pub_date']
    list_display = ['title', 'source',  'pub_date']


class NewsEnglishAdmin(admin.ModelAdmin):
    list_filter = ['source', 'category_en', 'pub_date']
    list_display = ['title', 'source',  'pub_date']


class NewsRussianAdmin(admin.ModelAdmin):
    list_filter = ['source', 'category_ru', 'pub_date']
    list_display = ['title', 'source', 'pub_date']


class RssAdmin(admin.ModelAdmin):
    list_display = ['name_tk', 'name_en', 'name_ru']


admin.site.register(CategoryTk)
admin.site.register(CategoryEn)
admin.site.register(CategoryRu)
admin.site.register(News, NewsAdmin)
admin.site.register(Rss, RssAdmin)
admin.site.register(NewsEnglish, NewsEnglishAdmin)
admin.site.register(NewsRussian, NewsRussianAdmin)
