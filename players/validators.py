import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class CustomUsernameValidator(object):
    message = _('Invalid username')

    def __call__(self, value):
        if not re.match(r"^[\w.]+#\d+$", value):
            raise ValidationError(self.message, code='invalid_username')


def username_validators():
    from allauth.socialaccount.providers.battlenet import validators
    return [
        validators.BattletagUsernameValidator
    ]