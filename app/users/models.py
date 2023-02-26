from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # define the custom permissions
    # related to User.
    class Meta:
        permissions = (
            ("Basic", "Can view 3 suggestions"),
            ("tier_2", "Can view 6 suggestions"),
            ('enterprise', 'can get binary image')
        )


    def __str__(self):
        return self.email