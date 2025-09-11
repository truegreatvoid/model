
from django.db import models


class Undefined(models.TextChoices):
    UNDEFINED = 'undefined', 'Indefinido'


UNDEFINED_HELP_TEXT = {
    Undefined.UNDEFINED: 'Tipo não definido.',
}
