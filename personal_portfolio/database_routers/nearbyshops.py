class NearbyShopsRouter:
    """
    A router to control all database operations on models in the
    nearbyshops application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read nearbyshops models go to geodjango.
        """
        if model._meta.app_label == 'nearbyshops':
            return 'geodjango'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write nearbyshops models go to geodjango.
        """
        if model._meta.app_label == 'nearbyshops':
            return 'geodjango'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the nearbyshops app is involved.
        """
        if obj1._meta.app_label == 'nearbyshops' or \
           obj2._meta.app_label == 'nearbyshops':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the nearbyshops app only appears in the 'geodjango'
        database.
        """
        if app_label == 'nearbyshops':
            return db == 'geodjango'
        return None