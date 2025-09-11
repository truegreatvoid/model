from django.db import models

from model_apps.model.boolean import BOOLEAN_ACTIVE_CHOICES
from model_apps.model.public_id import PublicID
from model_apps.model.softdelete import SoftDelete
from model_apps.model.timestamp import Timestamp


class BaseModel(
    PublicID,
    Timestamp,
    SoftDelete,
):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        default=True,
        db_index=True,
        choices=BOOLEAN_ACTIVE_CHOICES,
    )

    class Meta:
        abstract = True
        indexes = [
            models.Index(
                fields=[
                    'name',
                    'created_at',
                    'active',
                ],
                name='idx_name_created_active',
            ),
        ]
