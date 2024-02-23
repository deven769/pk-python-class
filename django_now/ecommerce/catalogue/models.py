from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length = 30)
	display_order = models.IntegerField(default = 1, null = True, blank = True)

	def __str__(self):
		return  self.name


class Product(models.Model):
	name = models.CharField(max_length = 50)
	category = models.ForeignKey(Category, related_name = 'category_product', on_delete = models.CASCADE)
	price = models.IntegerField(default = 0)
	quantity = models.IntegerField(default = 1)
	image = models.ImageField(upload_to = 'products', null= True, blank = True)
	description = models.CharField(max_length = 300, null = True, blank = True)
	related_products = models.ManyToManyField('self', blank = True)
	is_featured = models.BooleanField(default = False)
	is_best_seller = models.BooleanField(default = False)

	def __str__(self):
		return self.name