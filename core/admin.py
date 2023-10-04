from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


class NewsAdmin(admin.ModelAdmin):
    list_filter = ['source', 'category', 'pub_date']


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
