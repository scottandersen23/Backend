from django.forms import ModelForm
from .models import Payment

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['first_name', 'last_name', 'amount', 'cc', 'description']