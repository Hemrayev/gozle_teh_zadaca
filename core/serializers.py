from .models import *
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'source',
            'rss_feed',
            'title',
            'category',
            'content',
            'pub_date',
            'link',
            'image',
        ]


class NewsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEnglish
        fields = [
            'id',
            'source',
            'rss_feed',
            'title',
            'category',
            'content',
            'pub_date',
            'link',
            'image',
        ]


class NewsRussianSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsRussian
        fields = [
            'id',
            'source',
            'rss_feed',
            'title',
            'category',
            'content',
            'pub_date',
            'link',
            'image',
        ]
