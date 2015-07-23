from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)
	status = models.IntegerField(default=0)

	def __unicode__(self):
		return '{0}'.format(self.product.name)