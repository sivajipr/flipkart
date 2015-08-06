from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flipkart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    url(r'^merchants/', include('merchant.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^merchant', 'merchant.views.home'),
    url(r'^user', 'users.views.home'),
    url(r'^sign-up', 'users.views.sign_up_check'),
    url(r'^login', 'users.views.login_check'),
    # url(r'^', 'users.views.home'),


)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))