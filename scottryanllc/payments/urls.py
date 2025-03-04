from django.urls import path    
from . import views


urlpatterns = [
    path("", views.payments, name="payments"),
    path("payment/<str:pk>", views.payment, name="payment"),
    path("create-payment/", views.createPayment, name="create-payment")
]