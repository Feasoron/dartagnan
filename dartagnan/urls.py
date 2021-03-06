from django.contrib import admin
from django.conf.urls import patterns, include, url
from dartagnan import views
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

        # Examples:
        # url(r'^$', 'dartagnan.views.home', name='home'),
        # url(r'^dartagnan/', include('dartagnan.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
        url(r'^menu/', include('dartagnan.menu.urls')),
        url(r'^$', views.index, name='index')
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
