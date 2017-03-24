from django import forms
from players.models import Characters


class AddCharacterForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = ('character_name', 'character_realm')
