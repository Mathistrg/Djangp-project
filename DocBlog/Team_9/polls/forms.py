from django import forms

class QuestionSearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search Questions')