from image.models import Image
from image.serializers import ImageSerailzier
from image.permission import IsOwner
from rest_framework import viewsets
from django.conf import settings



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerailzier
    permission_classes = [IsOwner]