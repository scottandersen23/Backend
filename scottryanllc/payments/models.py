from django.db import models
import uuid

# Payment Table
class Payment(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=11, decimal_places=2,default=0) # when NULL is True, the col doesn't require data.
    cc = models.ManyToManyField('CC', blank=False) # blank here allows us to have a null field in a form.
    description = models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title
    

class CC(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name