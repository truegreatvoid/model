from django.conf import settings
from django.db import models
from django.utils import timezone

from model_apps.constant.boolean import BOOLEAN_DELETED_CHOICES
from model_apps.constant.permission import (
    Type as PermissionType,
)


class SoftDelete(models.Model):
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Deleted by user',
        related_name='deleted_%(class)s_set',
    )
    is_deleted = models.BooleanField(
        default=False,
        db_index=True,
        choices=BOOLEAN_DELETED_CHOICES,
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    last_operation = models.CharField(
        max_length=20,
        choices=PermissionType,
        null=True,
        blank=True,
    )

    def soft_delete(self, user):
        self.deleted_by = user
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.last_operation = PermissionType.SOFT_DELETE
        self.save(
            update_fields=[
                'is_deleted',
                'deleted_at',
                'deleted_by',
                'last_operation',
            ]
        )

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None
        self.last_operation = PermissionType.RESTORE
        self.save(
            update_fields=[
                'is_deleted',
                'deleted_at',
                'deleted_by',
                'last_operation',
            ]
        )

    class Meta:
        abstract = True
        indexes = [
            models.Index(
                name='idx_not_deleted',
                fields=['deleted_at'],
                condition=Q(is_deleted=False),
            ),
            models.Index(
                name='idx_not_del_and_delat',
                fields=[
                    'is_deleted',
                    'deleted_at',
                ],
            ),
        ]
