from django.db import models

# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    num = models.DecimalField(max_digits=10, decimal_places=0)
    gender = models.DecimalField(max_digits=1, decimal_places=0)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.name