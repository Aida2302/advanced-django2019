from django.db import models
from django.contrib.auth.models import AbstractUser

from users.constants import ROLES

class User(AbstractUser):
    # SuperAdmin, StoreAdmin, Guest
    # role = models.PositiveSmallIntegerField(choices=ROLES)
    is_super_admin = models.BooleanField(default=False)
    is_store_admin = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_login}'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
