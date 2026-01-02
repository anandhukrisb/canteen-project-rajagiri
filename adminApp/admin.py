from django.contrib import admin
from .models import (
    Product, ProductOption, ProductOptionChoice,
    Order, Seat, Lab, QRCode
)
from .utils.qr import generate_qr

# Regular model registrations
admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(ProductOptionChoice)
admin.site.register(Order)
admin.site.register(Seat)
admin.site.register(Lab)

# QRCode with actions
@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('seat', 'token', 'is_active')
    actions = ['generate_qr_codes'] 
    actions_on_top = True
    actions_on_bottom = True

    def generate_qr_codes(self, request, queryset):
        for qr in queryset:
            generate_qr(qr.token)
        self.message_user(request, "QR codes generated successfully")
