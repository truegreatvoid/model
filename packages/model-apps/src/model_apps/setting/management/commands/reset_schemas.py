from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Dropa e recria os schemas (module_schema e public), depois roda migrate.'

    def handle(self, *args, **options):
        schemas = [
            'module_schema',
            'public',
        ]

        with connection.cursor() as cursor:
            for s in schemas:
                cursor.execute(f'DROP SCHEMA IF EXISTS "{s}" CASCADE;')
                cursor.execute(f'CREATE SCHEMA "{s}";')
                self.stdout.write(self.style.SUCCESS(f'Schema "{s}" recriado com sucesso.'))

        self.stdout.write(self.style.NOTICE('Rodando migrações...'))
        call_command('migrate', interactive=False)

        self.stdout.write(self.style.SUCCESS('Reset completo: schemas recriados e migrações aplicadas.'))
