from django.conf.urls import patterns, url

from nachi import views

urlpatterns = patterns('',
    url(r'^$', views.customer, name='index'),
    url('/kitchen', views.kitchen, name='kitchen'),
    url('/customer', views.customer, name='customer'),
)
