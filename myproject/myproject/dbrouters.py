class TransactionDBRouter:
    """
    A router to control all database operations on models in the
    'orders' application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'orders':
            return 'transactions'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'orders':
            return 'transactions'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both objects are in the orders app
        if obj1._meta.app_label == 'orders' and \
           obj2._meta.app_label == 'orders':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'orders':
            return db == 'transactions'
        return None
