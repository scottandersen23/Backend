from django.db import models

# Create your models here.
class MyTable(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.IntegerField()

    def __str__(self):
        return self.column1

    