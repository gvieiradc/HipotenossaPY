from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse
from hipotenossa import settings

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug  = models.SlugField (max_length=255)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

   # def get_absolute_url(self):
     #   return reverse("pit:detail", kwargs=("slug": self.slug)


class User(AbstractUser):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique= True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


