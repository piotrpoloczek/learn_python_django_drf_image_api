from django.urls import path, include
from rest_framework.routers import DefaultRouter
from image import views



router = DefaultRouter()
router.register(r'images', views.ImageViewSet, basename='images')
router.register(r'thumbnails', views.ThumbnailViewSet, basename='thumbnails')


urlpatterns = [
    path('', include(router.urls)),
]