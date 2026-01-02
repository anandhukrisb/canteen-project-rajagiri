from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Seat, QRCode

@receiver(post_save, sender=Seat)
def create_qr_for_seat(sender, instance, created, **kwargs):
    if created:
        QRCode.objects.create(seat=instance)
