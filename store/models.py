from django.db import models
from .paystack import PayStack        
import secrets


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="category_images")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images")
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
#     customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date_created = models.DateTimeField(auto_now_add=True)
#     transaction_id = models.CharField(max_length=200)

#     def __str__(self):
#         return f"{self.product.name} - {self.customer.username}"


class PaystackPayment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='payments')
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.product.name} - Ref: {self.ref}"

    def amount_value(self):
        return self.amount * 100

    def verify_payment(self):
        payment = PayStack()
        status, result = payment.verify_payment(self.ref, self.amount)
        if status and result['amount'] / 100 == self.amount:
            self.verified = True
        self.save()
        return self.verified    