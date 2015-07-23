from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Merchant(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	company = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	address3 = models.CharField(max_length=100)
	phone_number = models.IntegerField(default=0)

