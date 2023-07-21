from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
            # Import and register your middleware here if needed
            from users.middleware import GetClientIPMiddleware