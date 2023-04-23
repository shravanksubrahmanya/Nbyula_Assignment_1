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

class Appointment(models.Model):
    terraformer = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name="creator")
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name="Enter the title of the meeting")
    agenda = models.TextField(verbose_name="Provide agenda of the meeting")
    guest = models.ForeignKey('accounts.CustomUser', verbose_name="Select the guest", on_delete=models.CASCADE, related_name="guest")
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Enter date of the meeting")
    start_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Enter start time of the meeting")
    end_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Enter end time of the meeting")

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Appointment_detail", kwargs={"pk": self.pk})
