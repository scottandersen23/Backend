# Register your models here.
from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription, Transaction

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'billing_period')
    search_fields = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'plan')
    search_fields = ('user__username',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user_subscription', 'amount', 'currency', 'timestamp', 'successful')
    list_filter = ('successful', 'currency')
    search_fields = ('transaction_id', 'user_subscription__user__username')
