# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SubscriptionPlan, UserSubscription
import datetime

def list_plans(request):
    """
    Display available subscription plans to the user.
    """
    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/list_plans.html', {'plans': plans})

@login_required
def subscribe(request, plan_id):
    """
    Subscribes the logged-in user to a chosen plan.
    (Actual payment/PayPal interaction would happen here or in a separate step.)
    """
    plan = get_object_or_404(SubscriptionPlan, id=plan_id)

    # Check if user already has an active subscription
    active_sub = UserSubscription.objects.filter(user=request.user, status='active').first()
    if active_sub:
        # Possibly cancel or switch plan logic here
        pass

    # Create new subscription record
    new_sub = UserSubscription.objects.create(
        user=request.user,
        plan=plan,
        status='active'  # would be updated to active upon successful payment confirmation
    )

    # In a real app, you'd redirect to a payment page or call PayPal's API
    return redirect('subscriptions:list_plans')

@login_required
def subscription_status(request):
    """
    Shows the user's current subscription status, if any.
    """
    user_sub = UserSubscription.objects.filter(user=request.user, status='active').first()
    return render(request, 'subscriptions/subscription_status.html', {'subscription': user_sub})
