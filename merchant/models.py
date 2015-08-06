from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Merchant(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	company = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	address3 = models.CharField(max_length=100)
	phone_number = models.CharField(default=0, max_length=12)

	def __unicode__(self):
		return '{0}'.format(self.user)

