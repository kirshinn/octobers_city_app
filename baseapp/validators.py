from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Пароль слишком короткий. Минимум %(min_length)d символов."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _("Пароль должен содержать минимум %(min_length)d символов.") % {'min_length': self.min_length}
