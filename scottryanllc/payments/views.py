from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment

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
