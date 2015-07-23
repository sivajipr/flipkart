from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.forms import MyAuthenticationForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flipkart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^sign-up', 'users.views.sign_up'),
    url(r'^login', 'users.views.log_in'),
    url(r'^logout', 'users.views.log_out'),
    url(r'^edit-profile', 'users.views.edit_profile'),
)
