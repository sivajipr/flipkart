from django.db import models
from merchant.models import Merchant
# Create your models here.
class Product(models.Model):
	CATEGORIES = (
			('Electronics','Electronic products'),
			('Cloathing','Clothings'),
			('Mobiles','Mobile products'),
			('Books','Book products'),
		)
	merchant = models.ForeignKey(Merchant)
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=20,choices=CATEGORIES)
	selling_price = models.IntegerField(default=0)
	original_price = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	photo = models.ImageField(upload_to="uploads/", null=True, blank=True)

	def __unicode__(self):
		return '{0}'.format(self.name)