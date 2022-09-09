from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(models.Model):
    username = models.CharField(max_length=16, unique=True, verbose_name=_('username'))
    first_name = models.CharField(max_length=50, verbose_name=_('first name'))
    last_name = models.CharField(max_length=50, verbose_name=_('last name'))
    password = models.CharField(max_length=255, verbose_name=_('password'))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
