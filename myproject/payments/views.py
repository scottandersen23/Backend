# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings

def payment_checkout(request):
    paypal_dict = {
        'business': 'your-paypal-merchant@example.com',  # or from settings
        'amount': '10.00',  # dynamically set this from your cart or context
        'item_name': 'Test Payment',
        'invoice': 'unique-invoice-id',
        'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
        'return_url': request.build_absolute_uri(reverse('payment_success')),
        'cancel_return': request.build_absolute_uri(reverse('payment_cancel')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    return render(request, 'payments/checkout.html', context)

def payment_success(request):
    # The user was redirected here by PayPal after success
    return render(request, 'payments/success.html')

def payment_cancel(request):
    # The user canceled the payment
    return render(request, 'payments/cancel.html')
