# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SubscriptionPlan(models.Model):
    """
    Defines various plans available for subscription.
    Example fields: name, price, billing_period (monthly, yearly), currency, etc.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')
    billing_period = models.CharField(max_length=20, default='monthly')  # or enum

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}/{self.billing_period}"


class UserSubscription(models.Model):
    """
    Tracks which plan a user is subscribed to, and the current status.
    """
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('past_due', 'Past Due'),
        ('canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} ({self.status})"


class Transaction(models.Model):
    """
    Records transactions for subscriptions, including PayPal transaction IDs, etc.
    """
    user_subscription = models.ForeignKey(UserSubscription, on_delete=models.CASCADE, related_name='transactions')
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=True)

    def __str__(self):
        return f"Txn {self.transaction_id} for {self.user_subscription}"
