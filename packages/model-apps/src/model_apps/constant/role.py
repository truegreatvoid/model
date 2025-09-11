from django.db import models


class Role(models.TextChoices):
    OWNER = 'owner', 'Proprietário'
    ADMIN = 'admin', 'Adminstrador'
    MEMBER = 'member', 'Membro'


ROLE_HELP_TEXT = {
    Role.OWNER.value: 'Usuário com controle total sobre a organização. Pode gerenciar configurações, usuários e permissões.',  # noqa: E501
    Role.ADMIN.value: 'Administrador com permissões amplas para gerenciar usuários e recursos, mas sem o controle total do proprietário.',  # noqa: E501
    Role.MEMBER.value: 'Usuário padrão com permissões limitadas, restrito às funcionalidades básicas da organização.',  # noqa: E501
}
