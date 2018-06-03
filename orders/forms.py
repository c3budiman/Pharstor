from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nama', 'email', 'alamat', 'kode_pos', 'kota']
