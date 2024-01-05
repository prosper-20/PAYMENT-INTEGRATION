import requests

from django.conf import settings

class PayStack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    base_url = "https://api.paystack.co"

def verify_payment(self, ref, *args, **kwargs):
    path = f"/transaction/verify/{ref}"
    headers = {
        "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    url = f"{self.base_url}{path}"
    response = requests.get(url, headers=headers).json()

    return response['status'], response['data'] if response['status_code'] == 200 else response['status'], response['message']
