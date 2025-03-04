from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Payment
from .forms import PaymentForm

paymentsList = [{'id': '1','title': "Payments Website", 'description': 'Full Stack Django Project'},{'id': '2','title': "Blog", 'description': 'Developing Software Applications'},{'id': '3','title': "Personal Portfolio", 'description': 'Professional Projects Folder'}]

def payment(request, pk):
    paymentObj = Payment.objects.get(id=pk)
    tags = paymentObj.tags.all()
    print('paymentObj', paymentObj)
    return render(request, 'payments/single-payments.html', {'payment':paymentObj, 'tags': tags})


def payments(request):
    payments = Payment.objects.all()
    context = {'payments': payments}
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