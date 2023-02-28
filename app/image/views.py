from image.models import Image, Thumbnail
from image.serializers import ImageSerailzier, ThumbnailSerializer
from image.permission import IsOwner
from rest_framework import viewsets
from django.conf import settings



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerailzier
    permission_classes = [IsOwner]


class ThumbnailViewSet(viewsets.ModelViewSet):
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer
    permission_classes = [IsOwner]