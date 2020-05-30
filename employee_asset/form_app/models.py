from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here

        

class BeaconAsset(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    work_location = models.CharField(max_length=200, blank = True,null=True)
    desktop = models.CharField(max_length=200, blank=True, null=True)
    laptop = models.CharField(max_length=200, blank=True, null=True)
    desk_phone = models.CharField(max_length=200, blank=True, null=True)
    single_monitor = models.CharField(max_length=200, blank=True, null=True)
    second_monitor = models.CharField(max_length=200, blank=True, null=True)
    third_monitor = models.CharField(max_length=200, blank=True, null=True)
    docking_station = models.CharField(max_length=200, blank=True, null=True)
    printer = models.CharField(max_length=200, blank=True, null=True)
    

    def get_absolute_url(self):
        return reverse("form_app:thank_you",)


    class Meta:
        ordering = ["last_name"]
    

    def __str__(self):
        return self.last_name



