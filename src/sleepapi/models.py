from django.db import models

# Create your models here.


class SleepCycleModel(models.Model):

    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE,null=True)
    sleepStruggle = models.IntegerField(null=True)
    sleepTime = models.IntegerField(null=True)
    wakeUpTime = models.IntegerField(null=True)
    sleepHours = models.IntegerField(null=True)
