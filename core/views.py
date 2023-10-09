from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class API(GenericAPIView):
    serializer_class = NewsSerializer

    def get(self, request):
        objects = News.objects.all()
        serializer = NewsSerializer(objects, many=True)
        return Response(serializer.data)


class API1(GenericAPIView):
    serializer_class = NewsEnglishSerializer

    def get(self, request):
        objects = News.objects.all()
        serializer = NewsEnglishSerializer(objects, many=True)
        return Response(serializer.data)


class API2(GenericAPIView):
    serializer_class = NewsRussianSerializer

    def get(self, request):
        objects = News.objects.all()
        serializer = NewsRussianSerializer(objects, many=True)
        return Response(serializer.data)
