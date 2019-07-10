from django.db import models
from datetime import datetime
from datetime import timedelta


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Worker(models.Model):
    # Accepts workers with only unique names
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    FREQ = (
        ("HOURLY", "Hourly"),
        ("DAILY", "Daily"),
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
        ("YEARLY", "Yearly"),
    )

    name = models.CharField(max_length=100, null=False)
    frequency = models.CharField(choices=FREQ, max_length=100)
    next_occurring_date = models.DateTimeField(null=True, blank=True)
    date_to_be_performed_by = models.DateTimeField(null=True, blank=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, blank=True, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.frequency == "HOURLY":
            self.next_occurring_date = datetime.now() + timedelta(hours=1)
        elif self.frequency == "DAILY":
            self.next_occurring_date = datetime.now() + timedelta(days=1)
        elif self.frequency == "WEEKLY":
            self.next_occurring_date = datetime.now() + timedelta(weeks=1)
        elif self.frequency == "MONTHLY":
            self.next_occurring_date = datetime.now() + timedelta(days=30)
        elif self.frequency == "YEARLY":
            self.next_occurring_date = datetime.now() + timedelta(days=365)

        super(Task, self).save(*args, **kwargs)
