class TCRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'tc':
            return 'school'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'tc':
            return 'school'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, **hints):
        if app_label == 'tc':
            return db == 'school'
        return db == 'default'
