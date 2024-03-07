from rest_framework import serializers
from catalogue.models import Category, Product

class CategorySerializers(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'



class ProductSerializers(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

