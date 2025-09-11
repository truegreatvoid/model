from enum import Enum


class OrgLimitType(str, Enum):
    USER = 'usuários'
    DEPARTMENT = 'departamentos'
    POSITION = 'ocupações'
    CLIENT = 'clientes'
