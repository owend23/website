# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class SeoConfig(SingletonModel):
    metrika_id = models.PositiveIntegerField(_('YA Metrika ID'), blank=True, null=True)
    end_title = models.CharField(_('End title'), max_length=64, blank=True, null=True)
    author = models.CharField(_('Author'), max_length=64, blank=True, null=True)
    keywords = models.CharField(_('Keywords'), max_length=128, blank=True, null=True)
    description = models.CharField(_('Description'), max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = _('SEO config')
        verbose_name_plural = _('SEO configs')
