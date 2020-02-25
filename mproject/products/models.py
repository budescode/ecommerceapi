from django.db import models
from messadmin.models import MessModel

class Products(models.Model):
	mess = models.ForeignKey(MessModel, on_delete = models.CASCADE)
	name = models.CharField(max_length=50)
	product_type = models.CharField(max_length=50, help_text='e.g veg/ non veg/ jain')
	details = models.TextField()
	specifications = models.CharField(max_length=50, help_text='e.g Lunch, dinner only or breakfast, lunch, dinner')
	available = models.BooleanField(default=True)