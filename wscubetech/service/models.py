from django.db import models
class Service (models.Model):
     service_course=models.CharField(max_length=50)
     service_about=models.CharField(max_length=50)

