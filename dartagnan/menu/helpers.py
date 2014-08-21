from django.template import RequestContext
from dartagnan.menu.models import RestaurantInfo

def get_context(request, values):
    rest_name =  RestaurantInfo.objects.first().name
    values['rest_name'] = rest_name
    values['founded'] = RestaurantInfo.objects.first().founded
    context =  RequestContext(request, values)
    return context