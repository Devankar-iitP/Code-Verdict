from django.db import models
from Authentication.models import detail

# Create your models here.
class question(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.DecimalField(max_digits=1, decimal_places=0)
    description = models.CharField(max_length=2000)
    in_format = models.CharField(max_length=1000, null=True)
    out_format = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

class testcase(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    inputs = models.CharField(max_length=2000)
    outputs = models.CharField(max_length=2000)

    def __str__(self):
        return self.question.name 
    
class attempt(models.Model):
    user = models.ForeignKey(detail, on_delete=models.CASCADE)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    num = models.PositiveIntegerField()
    status = models.DecimalField(max_digits=1, decimal_places=0)