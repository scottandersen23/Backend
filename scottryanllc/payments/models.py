from django.db import models
import uuid

# Payment Table
class Payment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # blank here allows us to have a null field in a form.
    demo_link = models.CharField(max_length=2000, null=True, blank=True) # when NULL is True, the col doesn't require data.
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name