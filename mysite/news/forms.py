from .models import Dann
from django.forms import ModelForm, TextInput

class DannForm(ModelForm):
	class Meta:
		model = Dann 
		fields =  ['name', 'massage', 'date']

		widgets = {
			"name": TextInput(attrs = {
					'class': 'inp name_massage',
					'placeholder': 'Ваше имя'
				}),

			"massage": TextInput(attrs = {
					'class': 'inp massage',
					'placeholder': 'Ваше сообщение'
				}),

			"date": TextInput(attrs = {
					'class': 'inp date_massage',
					'placeholder': 'Дата',
					'type': 'date'
				})
		}