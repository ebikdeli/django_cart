from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'

    def ready(self) -> None:
        # post_save.connect(create_cart_for_user, sender=settings.AUTH_USER_MODEL)
        from .models import Cart

        @receiver(post_save, sender=settings.AUTH_USER_MODEL)
        def create_cart_for_user(sender, instance, created, **kwargs):
            if created:
                Cart.objects.create(user=instance)
            try:
                cart = instance.cart_user
            except ValueError:
                Cart.objects.create(user=instance)