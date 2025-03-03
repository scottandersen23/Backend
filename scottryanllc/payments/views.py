from django.shortcuts import render
from django.http import HttpResponse

paymentsList = [{'id': '1','title': "Payments Website", 'description': 'Full Stack Django Project'},{'id': '2','title': "Blog", 'description': 'Developing Software Applications'},{'id': '3','title': "Personal Portfolio", 'description': 'Professional Projects Folder'}]

def payment(request, pk):
    paymentsObj = None
    for i in paymentsList:
        if i['id'] == pk:
            paymentsObj = i
    return render(request, 'payments/single-payments.html', {'payment':paymentsObj})


def payments(request):
    page = 'payments'
    number = 10
    context = {'page': page, 'number': number, 'payments': paymentsList}
    return render(request, 'payments/payments.html', context)
