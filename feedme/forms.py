from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class TitleForm(forms.Form):
    title__icontains = forms.CharField(required=False, label='video title', max_length=100)
    created__gte = forms.DateTimeField(required=False, label='Upload date no later than', widget=DateInput())


