from django.db import models

# Create your models here.
class Entree(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	image_url = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Menu(models.Model):
	name = models.CharField(max_length=10)
	entrees = models.ManyToManyField(Entree)

	def __unicode__(self):
		return self.name

class Order(models.Model):
	table_number = models.CharField(max_length=2)
	entrees = models.ManyToManyField(Entree)

	def __unicode__(self):

		return 'Table ' + self.table_number