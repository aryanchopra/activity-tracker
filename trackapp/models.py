from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class Activity(models.Model):
    date = models.DateField(default=now)
   
    owner = models.ForeignKey(to=User,on_delete = models.CASCADE)
   
    sleep= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(24)])

    qsleep=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    classes=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(12)])
  
    workout=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

    qday=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    project = models.CharField(max_length=255,default='None')

    phours= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(24)],default=0)
    class Meta:
        unique_together = (('date', 'owner'))
        ordering:['-date']
        verbose_name_plural='Activities'

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User,on_delete = models.CASCADE)
    details= models.TextField(default='None')
    def __str__(self):
        return self.name
