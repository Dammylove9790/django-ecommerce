from django.apps import AppConfig


class DjangoEcommerceAppConfig(AppConfig):
    name = 'django_ecommerce_app'
    
    def ready(self):
        import django_ecommerce_app.signals
