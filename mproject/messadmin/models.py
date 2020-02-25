from django.db import models
from django.contrib.auth import get_user_model

class MessModel(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
	name = models.CharField(max_length=200)
	address = models.TextField()
	number = models.CharField(max_length=20)
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username


class MessRules(models.Model):
	mess = models.ForeignKey(MessModel, on_delete=models.CASCADE)
	cancel_launch_before = models.TimeField()
	cancel_dinner_before = models.TimeField()
	breakfast_from = models.TimeField()
	breakfast_to = models.TimeField()
	launchtime_from = models.TimeField()
	launchtime_to = models.TimeField()
	dinnertime_from = models.TimeField()
	dinnertime_to = models.TimeField()