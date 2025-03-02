from django.urls import path    
from . import views


urlpatterns = [
    path("payments/", views.transactions, name="payments"),
    path("payment/<str:pk>", views.transaction, name="payment"),

]