from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
from tiers.models import Tier, Size
from sorl.thumbnail import get_thumbnail, ImageField
from django_resized import ResizedImageField
import PIL
from project import settings


class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.FileField(upload_to='pics')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_thumbnail()

        return self

    def create_thumbnail(self):
        sizes = self.author.tier.size.all()
        for size in sizes:
            height = int(str(size).split()[0])

            img = PIL.Image.open(self.photo.path)
            height_int = int(height)
            img = img.resize((height_int, height_int))
            path = self.photo.path + f'{height}.jpg'
            url = self.photo.url.replace("media/", "") + f'{height}.jpg'
            img.save(path)

            thumbnail = Thumbnail.objects.create(photo=self, height=height, miniature=url)


class Thumbnail(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image', null=True)
    miniature = models.FileField(upload_to='whatever')
    height = models.IntegerField()