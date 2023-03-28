from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.TextField()

    def get_absolute_url(self):
        return reverse("company-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(100)]
    )

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    

class Task(models.Model):
    text = models.TextField()
    done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})