from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
from tiers.models import Tier, Size
from sorl.thumbnail import get_thumbnail, ImageField



class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    author = models.ForeignKey(get_user_model(), related_name='images', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_thumbnail()
        return self

    def create_thumbnail(self):
        sizes = self.author.tier.size.all()
        
        for size in sizes:
            thumbnail = Thumbnail.objects.create(photo=self, height=str(size).split()[0], miniature=self.photo)


class Thumbnail(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image', null=True)
    miniature = ImageField(upload_to='thumbnails')
    height = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.miniature = get_thumbnail(self.miniature, '200x200', quality=99, format='JPEG').url
        self.save()
        return self