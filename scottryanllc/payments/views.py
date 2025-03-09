from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Payment
from .forms import PaymentForm

paymentsList = [{'id': '1','first_name': "Ari", 'last_name': 'Doodle', 'amount':'$100.00', 'CreditCard': 'Chase Freedom', 'description':'memory foam dog bed'},
                {'id': '2','first_name': "Nicole", 'last_name': 'Cabrera', 'amount':'$250.00', 'CreditCard': 'American Express', 'description':'lashes, brows, nails and toes'},
                {'id': '3','first_name': "Cooper", 'last_name': 'Andersen', 'amount':'$75.00', 'CreditCard': 'Paypal', 'description':'body scrub and facial'}]

def payment(request, pk):
    paymentObj = Payment.objects.get(id=pk)
    creditcard = paymentObj.CreditCard.all()
    print('paymentObj', paymentObj)
    return render(request, 'payments/single-payments.html', {'payment':paymentObj, 'CreditCard':creditcard})


def payments(request):
    payments = Payment.objects.all()
    context = {'payment': payments}
    return render(request, 'payments/payments.html', context)

def createPayment(request):
    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments')
        
    context = {'form': form}
    return render(request, "payments/payment_form.html", context)

def updatePayment(request,pk):
    payment = Payment.objects.get(id=pk)
    form = PaymentForm(instance=payment)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payments')
        
    context = {'form': form}
    return render(request, "payments/payment_form.html", context)