from django import forms


# Поля этой формы совпадают с полями модели Tournament -
# можно было бы использовать ModelForm
# (https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/)
class TournamentForm(forms.Form):
    name = forms.CharField()
    date = forms.DateField(required=False)
