from django import forms
from catalogue.models import Category, Product
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'

		widgets = {
        	'name': forms.TextInput(attrs=({'placeholder': 'Enter category Name','class': 'form-control'})),
        	'display_order': forms.NumberInput(attrs=({'placeholder': 'Enter display ORder','class': 'form-control'})),
        }

	def clean(self):
		data = super().clean()
		name = data.get('name')
		if Category.objects.filter(name = name).exists():
			raise ValidationError('Name Already exists =-----')
		return data


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
