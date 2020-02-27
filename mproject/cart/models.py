from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    amount = models.DecimalField(default=0.00, max_digits = 30, decimal_places = 2)
    qty = models.PositiveIntegerField()
    date = models.DateField(auto_now_add = True)
