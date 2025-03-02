from django.shortcuts import render
from django.http import HttpResponse


def payment(request, pk):
    return HttpResponse('Searching for Payment_ID: ' + str(pk))


def payments(request):
    return HttpResponse('Here is your payment history.')