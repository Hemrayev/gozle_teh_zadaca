from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class NewsAdmin(admin.ModelAdmin):
    list_filter = ['source', 'category', 'pub_date']


class RssAdmin(admin.ModelAdmin):
    list_display = ['name_tk', 'name_en', 'name_ru']


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Source)
admin.site.register(Rss, RssAdmin)
