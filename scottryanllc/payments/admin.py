from django.contrib import admin
from .models import Payment, CreditCard

admin.site.register(Payment)
admin.site.register(CreditCard)