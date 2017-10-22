from django.db import models

class Entry(models.Model):
    machine_id = models.CharField(max_length=20)
    machine_model = models.CharField(max_length=20)
    max_load = models.IntegerField()
    current_weight = models.IntegerField()

