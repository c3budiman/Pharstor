from django.contrib import admin

from orders.models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['nama', 'email', 'alamat', 'kode_pos', 'kota', 'created', 'updated', 'sudah_dibayar']
    list_editable = ['email', 'alamat', 'sudah_dibayar']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
    list_editable = ['product', 'quantity']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
