from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import QRCode


def admin_page(request):
    return render(request, 'AdminDashboard.html')



def place_order(request, token):
    qr = get_object_or_404(QRCode, token=token, is_active=True)
    seat = qr.seat
    lab = seat.lab

