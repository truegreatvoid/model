from django.db import models


class Status(models.TextChoices):
    UNDEFINED = 'undefined', 'Indefinido'
    CLIENT = 'client', 'Cliente'
    FORMER_CLIENT = 'former_client', 'Ex-cliente'
    PROSPECT = 'prospect', 'Potencial cliente'
    PARTNER = 'partner', 'Parceiro'


class Type(models.TextChoices):
    UNDEFINED = 'undefined', 'Indefinido'
    HEADOFFICE = 'head_office', 'Matriz'
    BRANCHOFFICE = 'branch_office', 'Filial'


STATUS_HELP_TEXT = {
    Status.UNDEFINED: 'Tipo de cliente não definido, ainda não classificado.',
    Status.CLIENT: 'Cliente ativo com contrato vigente ou relacionamento atual.',
    Status.FORMER_CLIENT: 'Empresa que já foi cliente, mas atualmente não possui vínculo ativo.',
    Status.PROSPECT: 'Empresa com potencial para se tornar cliente; em fase de prospecção.',
    Status.PARTNER: 'Empresa parceira com colaboração estratégica, mas que não é cliente direto.',
}
