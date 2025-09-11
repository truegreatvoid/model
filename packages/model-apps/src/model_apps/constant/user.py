from django.db import models


class Status(models.TextChoices):
    ACTIVE = 'active', 'Ativo'
    INACTIVE = 'inactive', 'Desativado'
    ON_VACATION = 'vacation', 'Férias'
    SICK_LEAVE = 'sick_leave', 'Atestado'
    SUSPENDED = 'suspended', 'Suspenso'
    TRAINING = 'training', 'Treinamento'
    ONBOARDING = 'onboarding', 'Integração'
    DISMISSED = 'dismissed', 'Demitido'


STATUS_HELP_TEXT = {
    Status.ACTIVE: 'O colaborador está ativo e operando normalmente.',
    Status.INACTIVE: 'O colaborador está inativo, mas ainda registrado no sistema.',
    Status.ON_VACATION: 'O colaborador está de férias.',
    Status.SICK_LEAVE: 'O colaborador está ausente por motivos de saúde.',
    Status.SUSPENDED: 'O vínculo com o colaborador está temporariamente suspenso.',
    Status.TRAINING: 'O colaborador está em período de treinamento.',
    Status.ONBOARDING: 'O colaborador está em processo de integração inicial.',
    Status.DISMISSED: 'O vínculo com o colaborador foi encerrado (demitido/desligado).',
}
