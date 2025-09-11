BOOLEAN_ACTIVE = {
    True: 'Ativo',
    False: 'Inativo',
}


BOOLEAN_ACCESS = {
    True: 'Liberado',
    False: 'Bloqueado',
}


BOOLEAN_STAFF = {
    True: 'Administrador',
    False: 'Usuário',
}


BOOLEAN_DELETED = {
    True: 'Deletado',
    False: 'Não deletado',
}


BOOLEAN_FROM_ME = {
    True: 'Enviado',
    False: 'Recebido',
}


BOOLEAN_ACTIVE_CHOICES = [
    (True, BOOLEAN_ACTIVE[True]),
    (False, BOOLEAN_ACTIVE[False]),
]


BOOLEAN_ACCESS_CHOICES = [
    (True, BOOLEAN_ACCESS[True]),
    (False, BOOLEAN_ACCESS[False]),
]


BOOLEAN_STAFF_CHOICES = [
    (True, BOOLEAN_STAFF[True]),
    (False, BOOLEAN_STAFF[False]),
]


BOOLEAN_DELETED_CHOICES = [
    (True, BOOLEAN_DELETED[True]),
    (False, BOOLEAN_DELETED[False]),
]


BOOLEAN_FROM_ME_CHOICES = [
    (True, BOOLEAN_FROM_ME[True]),
    (False, BOOLEAN_FROM_ME[False]),
]
