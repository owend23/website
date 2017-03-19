# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import reverse
from django_webtest import WebTest
from django_dynamic_fixture import G
from django.contrib.sites.models import Site


class HomeViewTest(WebTest):
    def setUp(self):
        self.site = G(
            Site,
            name='Site2',
            domain='example2.com'
        )

    def test_view(self):
        url = reverse('home')
        res = self.app.get(url)

        self.assertEquals(res.status_code, 200)
