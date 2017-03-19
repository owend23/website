# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from apps.common.sitemaps import sitemaps_content
from apps.common.views import (
    HomePageView, FaviconRedirectView
)
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^favicon\.ico', FaviconRedirectView.as_view(), name='favicon'),
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^sitemap\.xml', sitemap, {'sitemaps': sitemaps_content}, name='sitemap')
]
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^admin/redactor/', include('redactor.urls')),
    ]

    urlpatterns += staticfiles_urlpatterns(prefix=settings.STATIC_URL)
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^admin.php', include('admin_honeypot.urls')),

        url(r'^admin-secret/', include(admin.site.urls)),
        url(r'^admin-secret/redactor/', include('redactor.urls')),
    ]

handler400 = 'apps.common.views.handler400'
handler403 = 'apps.common.views.handler403'
handler404 = 'apps.common.views.handler404'
handler500 = 'apps.common.views.handler500'
