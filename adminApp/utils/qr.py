import qrcode
from django.conf import settings
from pathlib import Path

def generate_qr(token):
    url = f"{settings.SITE_URL}/order/{token}/"

    qr = qrcode.make(url)

    qr_dir = Path(settings.MEDIA_ROOT) / "qrcodes"
    qr_dir.mkdir(parents=True, exist_ok=True)

    file_path = qr_dir / f"{token}.png"
    qr.save(file_path)

    return f"qrcodes/{token}.png"
