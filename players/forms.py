from django import forms
from players.models import Characters
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class MyValidator(UnicodeUsernameValidator):
    regex = r"^[\w.]+#\d+$"


class MyUser(User):
    username_validator = MyValidator

    class Meta:
        proxy = True  # If no new field is added.


class AddCharacterForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = ('character_name', 'character_realm')
