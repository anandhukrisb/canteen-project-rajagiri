from django.db import models



class Lab(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} -- {self.is_active}'

class QRCode(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    token = models.UUIDField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.is_active
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.product.name} -- {self.name}'
    
class ProductOptionChoice(models.Model):
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.option.name} -- {self.value}'
    
class Order(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
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

