from django import forms
from players.models import Realms


class CreateGuildForm(forms.Form):
    guild_name = forms.CharField(max_length=50)
    guild_realm = forms.ModelChoiceField(queryset=Realms.objects.all())
    
