from django.db import models

from shop.models import Product


class Order(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    alamat = models.CharField(max_length=250)
    kode_pos = models.CharField(max_length=10)
    kota = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sudah_dibayar = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity
