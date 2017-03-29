from django.contrib.admin import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

username_regex_field = forms.RegexField(
    label="Username",
    max_length=30,
    regex=r"^[\w.]+#\d+$",
    help_text="Required. 30 characters or fewer. Letters, apostrophes, periods, hyphens and at signs.",
    error_message="This value must contain only letters, apostrophes, periods, hyphens and at signs."
)


class UserCreationForm(UserCreationForm):
    username = username_regex_field


class UserChangeForm(UserChangeForm):
    username = username_regex_field


class UserProfileAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm