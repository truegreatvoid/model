from django.db import models


class Email(models.Model):
    """
    Email field permanece como unique, porque pode apenas conter um email por usuário independente da organização.
    """

    email = models.EmailField(
        unique=True,
        db_index=True,
    )

    class Meta:
        abstract = True
