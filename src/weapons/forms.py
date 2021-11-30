from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Название предмета', max_length=20)