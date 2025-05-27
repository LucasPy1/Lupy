from django.db import models

class UserModel(models.Model):  # Use CapWords convention

    id = ...
    name = models.CharField(max_length=100)

class SkillModel(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    level = models.PositiveSmallIntegerField()  # I can change to SmallIntegerField if needed, it holds higher nums.
    date_started_learning = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
