from django.db import models


class Status(models.TextChoices):
    CREATE = 'create', 'Criar'
    READ = 'read', 'Visualizar'
    UPDATE = 'update', 'Editar'
    DELETE = 'delete', 'Remover'
    ACCESS_MODULE = 'access_module', 'Acessar Módulo'
    NOTIFICATION = 'notification', 'Receber Notificações'
    OTHER = 'other', 'Outros'
    SOFT_DELETE = 'soft_delete', 'Inativar'
    RESTORE = 'restore', 'Reativar'


STATUS_HELP_TEXT = {
    Status.CREATE: 'Permite criar novos registros ou recursos.',
    Status.READ: 'Permite visualizar registros ou informações.',
    Status.UPDATE: 'Permite editar ou atualizar registros existentes.',
    Status.DELETE: 'Permite remover ou excluir registros do sistema.',
    Status.ACCESS_MODULE: 'Permite acessar e visualizar um módulo específico da aplicação.',
    Status.NOTIFICATION: 'Permite receber notificações relacionadas à atividade ou sistema.',
    Status.OTHER: 'Permissão genérica para ações não categorizadas nas opções anteriores.',
    Status.SOFT_DELETE: 'Permite inativar um registro.',
    Status.RESTORE: 'Permite reativar um registro inativo.',
}
