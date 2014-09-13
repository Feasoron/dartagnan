from django.http import HttpResponse
from django.template import loader
from dartagnan.menu.models import RestaurantInfo
from dartagnan.menu.models import Location
from dartagnan.menu.helpers import get_context


def index(request):
    locations = Location.objects.all()
    template = loader.get_template('index.html')
    context = get_context(request, {
        'locations': locations
    })
    return HttpResponse(template.render(context))