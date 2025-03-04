from django.contrib import admin

# Register your models here.
from .models import Payment, Tag

admin.site.register(Payment)
admin.site.register(Tag)