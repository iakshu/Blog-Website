from django import forms
from .models import BgModel

class BgForm(forms.ModelForm):
	class Meta:
		model = BgModel
		fields = ( 'title', 'author', 'body',)

		labels = {
			'title':'',
			'author':'',
			'body': '',
		}

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','id':'title',}),
			'author': forms.TextInput(attrs={'class': 'form-control','id':'author', 'value':'', 'type':'hidden'}),
			#'body': forms.Textarea(attrs={'class': 'form-control'}),
		}
