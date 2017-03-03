from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class TitleForm(forms.Form):
    title__icontains = forms.CharField(required=False, label='video title', max_length=100)
   # created__gte = forms.DateField(required=False, label='Upload date no later than',widget=DateInput(),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'])
    created__gte = forms.DateTimeField(required=False, label='Upload date no later than', initial='2000-01-01')


