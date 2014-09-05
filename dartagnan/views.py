from django.http import HttpResponse
from django.template import loader
from dartagnan.menu.models import RestaurantInfo
from dartagnan.menu.models import Category
from dartagnan.menu.helpers import get_context


def index(request):
    rest_info = RestaurantInfo.objects.first()
    locations = rest_info.location_set.all()
    template = loader.get_template('index.html')
    context = get_context(request, {
        'locations': locations
    })
    return HttpResponse(template.render(context))