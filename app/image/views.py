from image.models import Image, Thumbnail
from image.serializers import ImageSerailzier, ThumbnailSerializer
from image.permission import IsOwner
from rest_framework import viewsets
from rest_framework import permissions
from django.conf import settings


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerailzier
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset


class ThumbnailViewSet(viewsets.ModelViewSet):
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset