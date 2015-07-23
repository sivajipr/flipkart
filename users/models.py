from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	place = models.CharField(max_length=200)


def create_profile(sender, instance, created, raw, **kwargs):
	"""Fleshes out the profile for the newly created user"""
	if created:
		profile = Profile(user=instance)
		profile.save()


post_save.connect(create_profile, sender=User,
dispatch_uid='users.models.create_profile')