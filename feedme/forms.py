from django import forms

class TitleForm(forms.Form):
    title__icontains = forms.CharField(required=False,label='video title', max_length=100)
    created__gte = forms.DateTimeField(required=False)


