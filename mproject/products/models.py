from django.db import models
from django.contrib.auth import get_user_model

class Products(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(default=0.00, decimal_places = 2, max_digits = 30)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)