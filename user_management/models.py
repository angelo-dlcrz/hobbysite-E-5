from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class ProxyUser(User):
    pass

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = 'user'


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField()

    def __str__(self) -> str:
        return self.display_name

    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(
                user=instance, 
                display_name=instance.username, 
                email_address=instance.email,
            )

    post_save.connect(create_profile, sender=User)
