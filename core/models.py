from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.TextField()

    def get_absolute_url(self):
        return reverse("company-detail", kwargs={"pk": self.pk})
    