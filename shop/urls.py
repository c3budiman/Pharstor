from django.conf.urls import url

from shop import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^category/(?P<category_slug>[\w\-]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^product/(?P<product_slug>[\w\-]+)/$', views.product_detail, name='product_detail'),
    url(r'^tentang/$', views.laman_tentang, name='laman_tentang'),
    url(r'^garansi/$', views.laman_garansi, name='laman_garansi'),
    url(r'^howtoorder/$', views.laman_howtoorder, name='laman_howtoorder'),
]
