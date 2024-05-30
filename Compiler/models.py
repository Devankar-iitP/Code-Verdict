from django.db import models
from Authentication.models import detail
from Problem.models import question

# Create your models here.
class info(models.Model):
    user = models.ForeignKey(detail, on_delete=models.CASCADE)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    language = models.CharField(max_length = 20)
    code = models.TextField()
    time = models.DateTimeField()