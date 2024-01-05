from django.contrib import admin
from .models import Category, Product, PaystackPayment

admin.site.register([Category, Product, PaystackPayment])
