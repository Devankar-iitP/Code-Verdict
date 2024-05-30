from django.db import models

# Create your models here.
class question(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.DecimalField(max_digits=1, decimal_places=0)
    description = models.TextField(null=True)
    in_format = models.TextField(null=True)
    out_format = models.TextField(null=True)
    type_name = models.IntegerField(default='1')

    def __str__(self):
        return self.name

class testcase(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    inputs = models.TextField(null=True)
    outputs = models.TextField(null=True)

    def __str__(self):
        return self.question.name 