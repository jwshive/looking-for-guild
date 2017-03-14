class BlizzardApiRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'players':
            return 'blizzard_api'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'players':
            return 'blizzard_api'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'players' or obj2._meta.app_label == 'players':
            return True
        return None

    def allow_syncdb(self, db, model):

        if db == 'blizzard_api':
            return model._meta.app_label == 'players'
        elif model._meta.app_label == 'players':
            return False
        return None