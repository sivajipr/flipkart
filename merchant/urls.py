from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flipkart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^sign-up', 'merchant.views.sign_up'),
    url(r'^login', 'merchant.views.log_in'),
    url(r'^product/(?P<p_id>[0-9]{1,})', 'merchant.views.show_product'),
	 
)
