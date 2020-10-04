import os
from django.shortcuts import render

APP_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

SITE_NAME = 'site1.ru'
# SITE_NAME = 'atv-rental.ru'


def simple_renderer(request, template_filename):
    template = "/".join([APP_NAME, SITE_NAME, template_filename])
    context = {'static_prefix': "/".join(
        [APP_NAME, SITE_NAME, template.rsplit('/', 2)[-1].rsplit('.', 2)[0], ''])}
    return render(request, template, context)


def index(request):
    return simple_renderer(request, "market_v2_index.html")


def service_detail(request):
    return simple_renderer(request, "service_detail.html")


def service_list(request):
    return simple_renderer(request, "service_list.html")
