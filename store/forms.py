from django import forms
from .models import PaystackPayment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaystackPayment
        fields = ["email", "amount"]