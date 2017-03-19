# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template import loader
from django.http import HttpResponse
from django.views.generic import (TemplateView, RedirectView)
from django.contrib.staticfiles.templatetags.staticfiles import static

logger = logging.getLogger('django.request')


class HomePageView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        kwargs.update({

        })
        return super(HomePageView, self).get_context_data(**kwargs)


class FaviconRedirectView(RedirectView):
    permanent = True
    url = '/static/'

    def get_redirect_url(self, *args, **kwargs):
        return static('favicon/favicon.ico')


def handler400(request):
    return _process_request(request, 400)


def handler403(request):
    return _process_request(request, 403)


def handler404(request):
    return _process_request(request, 404)


def handler500(request):
    return _process_request(request, 500)


def _process_request(request, code):
    # type: (request, int) -> request
    template_path = 'common/{}.html'.format(code)
    try:
        template = loader.get_template(template_path)
    except TemplateDoesNotExist:
        msg = 'Template path "{}" does not exists'.format(
            template_path
        )
        logger.warn(msg)

        handler_path = 'django.conf.urls.handler{}'.format(code)
        handler = __import__(handler_path)
        return handler()

    context = {
        'request': request,
        'STATIC_URL': settings.STATIC_URL,
    }
    body = template.render(context, request)
    return HttpResponse(body, code=code)
