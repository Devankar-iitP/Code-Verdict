from django.contrib import admin
from .models import question, testcase, attempt

# Register your models here.
admin.site.register(question)
admin.site.register(testcase)
admin.site.register(attempt)