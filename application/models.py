from django.db import models

# Create your models here.
class promotiontable(models.Model):
    performance = models.CharField(max_length = 100)
    seniority = models.CharField(max_length = 100)
    assesments = models.CharField(max_length = 100)
    time_sence = models.CharField(max_length = 100)
    elgibility = models.CharField(max_length = 10)
