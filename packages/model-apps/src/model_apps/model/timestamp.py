from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['created_at', 'updated_at'], name='idx_tt_created_updated'),
        ]
