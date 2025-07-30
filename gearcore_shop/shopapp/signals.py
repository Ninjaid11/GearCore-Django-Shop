import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

logger = logging.getLogger("shopapp")

@receiver(post_save, sender=Product)
def link_brand_to_category(sender, instance, created, **kwargs):
    if created:
        brand = instance.brand
        category = instance.category
        if not brand.category.filter(id=category.id).exists():
            brand.category.add(category)
            logger.info(f"Добавлена связь: бренд '{brand.name}'  категория '{category.name}'")