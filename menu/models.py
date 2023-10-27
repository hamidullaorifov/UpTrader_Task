from django.db import models
from django.urls import reverse
# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"path": self.name})
    