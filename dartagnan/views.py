from django.http import HttpResponse
from django.template import RequestContext, loader
from dartagnan.menu.models import RestaurantInfo


def index(request):
    rest_info = RestaurantInfo.objects.first()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
            'rest_info': rest_info
    })
    return HttpResponse(template.render(context))