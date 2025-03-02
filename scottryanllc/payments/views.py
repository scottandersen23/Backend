from django.shortcuts import render
from django.http import HttpResponse


def transaction(request, pk):
    return render(request, 'single-payments.html')


def transactions(request):
    return render(request, 'payments.html')
