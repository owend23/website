# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import reverse
from django.contrib import sitemaps


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


sitemaps_content = {
    'static': StaticViewSitemap,
}
