from django.conf.urls import patterns, include, url
from django.contrib import admin
import cart

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flipkart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^add_to_cart/(?P<id>[0-9]{1,})', 'cart.views.add_to_cart'),
    url(r'^cart_list', 'cart.views.cart_list'),
    url(r'^add', 'product.views.add_product'),
    url(r'^(?P<id>[0-9]{1,})', 'product.views.show_product'),
    url(r'^buy-now/(?P<address_id>[0-9]{1,})/(?P<product_id>[0-9]{1,})', 'product.views.buy_product'),
    url(r'^buyerror/(?P<id>[0-9]{1,})', 'product.views.buyerror'),	   
)
