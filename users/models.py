from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from product.models import Product
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	place = models.CharField(max_length=200)

class Address(models.Model):
	user = models.ForeignKey(User)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	address3 = models.CharField(max_length=100)
	pincode = models.IntegerField(max_length=12)
	phone_number = models.CharField(max_length=12)

	def __unicode__(self):
		return '{0}'.format(self.address1)

class Buy(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	address = models.ForeignKey(Address)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=1)
	status = models.IntegerField(default=0)
	create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


def create_profile(sender, instance, created, raw, **kwargs):
	"""Fleshes out the profile for the newly created user"""
	if created:
		profile = Profile(user=instance)
		profile.save()


post_save.connect(create_profile, sender=User,
dispatch_uid='users.models.create_profile')