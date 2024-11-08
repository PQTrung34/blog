from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.body)
    
    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse('home')