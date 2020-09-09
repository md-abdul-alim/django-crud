from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    emp_id     = models.CharField(max_length=3)
    mobile     = models.CharField(max_length=15)
    position   = models.ForeignKey(Position, on_delete=models.CASCADE)