from django.db import models

# Create your models here.
from django.db import models

class PayPalTransaction(models.Model):
    paypal_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)  # e.g., 'Completed', 'Pending'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paypal_id} - {self.status}"
