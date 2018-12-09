from django import forms


class search(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    genre = forms.CharField(label='genre', max_length=100)