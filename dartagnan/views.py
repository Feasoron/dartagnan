from django.http import HttpResponse
from django.template import loader
from dartagnan.menu.models import RestaurantInfo
from dartagnan.menu.models import Category
from dartagnan.menu.helpers import get_context


def index(request):
    rest_info = RestaurantInfo.objects.first()
    template = loader.get_template('index.html')
    context = get_context(request, {
        'restaurant_name': rest_info.name,
        'rest_info': rest_info,
        'categories': Category.objects.all()
    })
    return HttpResponse(template.render(context))