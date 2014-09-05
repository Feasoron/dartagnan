from django.conf.urls import patterns, url
from dartagnan.menu import views


urlpatterns = patterns('',
    url(r'^$', views.menu, name='menu'),
    url(r'^category/(?P<category_name>\w+)', views.category, name='category'),
    url(r'^about$', views.about_us, name='about_us'),
    url(r'^locations$', views.locations, name='locations')
)