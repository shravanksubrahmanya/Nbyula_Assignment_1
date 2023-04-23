from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class OffHour(models.Model):
    terraformer = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Enter date", null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Enter start time")
    end_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Enter end time")
    class Meta:
        verbose_name = "OffHour"
        verbose_name_plural = "OffHours"

    def __str__(self):
        return f"{self.terraformer} ({self.start_time} - {self.end_time})"

    def get_absolute_url(self):
        return reverse("OffHours_detail", kwargs={"pk": self.pk})
