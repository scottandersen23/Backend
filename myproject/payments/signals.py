from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from orders.models import Transaction

@receiver(valid_ipn_received)
def paypal_payment_success(sender, **kwargs):
    ipn_obj = sender
    # Check if the payment_status is "Completed"
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Create transaction in the transactions database
        Transaction.objects.using('transactions').create(
            user_id=ipn_obj.custom,   # Maybe you passed user_id in `custom`
            amount=ipn_obj.mc_gross
        )
        # Fire off your custom signal if you like:
        # payment_successful.send(sender=Transaction, transaction_id=new_transaction.id)
