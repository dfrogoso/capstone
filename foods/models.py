from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.price)
