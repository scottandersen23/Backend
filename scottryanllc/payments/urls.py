from django.urls import path    
from . import views


url_patterns = [
    path("payment/<str:pk>", views.payment, name="payment"),
    path("payments/", views.payments, name="payments")

]