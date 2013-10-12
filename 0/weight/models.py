from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 64)
	password = models.CharField(max_length = 64)
	status   = models.CharField(max_length = 20)
	weight_delta = models.DecimalField(max_digits=4, decimal_places=1, default=0)

	def __unicode__(self):
		return self.username

class WeightRecord(models.Model):
	user = models.ForeignKey(User)
	date = models.DateField('data published', auto_now_add=True)
	weight = models.DecimalField(max_digits=4, decimal_places=1)
