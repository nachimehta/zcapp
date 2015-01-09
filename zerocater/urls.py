from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zerocater.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('nachi.urls')),
    url(r'^customer/', 'nachi.views.customer', name='customer'),
    url(r'^kitchen/', 'nachi.views.kitchen', name='kitchen'),
    url(r'^place_order/', 'nachi.views.place_order'),
    url(r'^delete_order/', 'nachi.views.delete_order'),
    url(r'^change_menu/', 'nachi.views.change_menu')
)
