from django.db import connection


class SchemaRouter:
    module_schema_apps = {
        'module.core',
        'module.organization',
        'module.authentication',
        'module.permission',
        'module.customers',
        'module.position',
        'module.client',
        'module.department',
    }

    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        full_app_label = self._get_full_app_label(app_label)

        if full_app_label in self.module_schema_apps:
            with connection.cursor() as cursor:
                cursor.execute('SET LOCAL search_path TO module_schema;')
            return True
        else:
            with connection.cursor() as cursor:
                cursor.execute('SET LOCAL search_path TO public;')
            return True

    def _get_full_app_label(self, app_label: str) -> str:
        for full_name in self.module_schema_apps:
            if full_name.split('.')[-1] == app_label:
                return full_name
        return app_label
