import uuid
from django.db import models


class Lab(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('lab', 'seat_number')

    def __str__(self):
        return f'{self.lab.code} - {self.seat_number}'


class QRCode(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'QR | {self.seat} | {self.token}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.product.name} - {self.name}'


class ProductOptionChoice(models.Model):
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.option.name}: {self.value}'


class Order(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[
            ('NEW', 'New'),
            ('ACK', 'Acknowledged'),
            ('PROG', 'In Progress'),
            ('DONE', 'Completed'),
            ('CANCEL', 'Cancelled'),
        ],
        default='NEW'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} | {self.lab.code} | {self.seat.seat_number}'


class OrderOption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    choice = models.ForeignKey(ProductOptionChoice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.option.name}: {self.choice.value}'
