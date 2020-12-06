from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem creation or update """
    instance.order.update_grand_total()
    instance.order.update_points_earned()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_grand_total()
    instance.order.update_points_earned()
