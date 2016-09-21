import os

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template import loader


def index(request):
    template = loader.get_template('index.html', dirs=[os.path.join(settings.BASE_DIR, 'templates')])
    context = RequestContext(request, {
        "debug": settings.DEBUG
    })
    return HttpResponse(template.render(context))