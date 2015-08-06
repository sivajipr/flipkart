from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.forms import MyAuthenticationForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flipkart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login-popup', 'users.views.login_popup'),
	url(r'^signup-popup', 'users.views.signup_popup'),
    url(r'^sign-up', 'users.views.sign_up'),
    url(r'^login', 'users.views.log_in'),
    url(r'^logout', 'users.views.log_out'),
    url(r'^edit-profile', 'users.views.edit_profile'),
    url(r'^forget-password', 'users.views.forget_password'),
    url(r'^newpassword/(?P<user>[\w\W]+)', 'users.views.new_password'),
    url(r'^address-verify/(?P<id>[0-9]{1,})', 'users.views.address_verify'),
	url(r'^addressadd/(?P<id>[0-9]{1,})', 'users.views.address_verify'),
	url(r'^address/(?P<id>[0-9]{1,})', 'users.views.address_delete'),
	url(r'^buyed-products', 'users.views.buyed_products'),
    url(r'^usersearch', 'users.views.usersearch'),
    url(r'^autocomplete', 'users.views.auto_complete'),
	)
