from rest_framework import serializers
from django.contrib.auth.models import User
from image.models import Image, Thumbnail


class ImageSerailzier(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['author', 'title', 'photo']


class ThumbnailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = ['height', 'photo', 'miniature']