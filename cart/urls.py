from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flipkart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cart_list', 'cart.views.cart_list'),
    url(r'^remove/(?P<id>[0-9]{1,})', 'cart.views.remove_cart'),

)
