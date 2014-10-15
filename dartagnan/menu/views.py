from django.http import HttpResponse
from dartagnan.menu.models import Category, RestaurantInfo, Location
from dartagnan.menu.helpers import get_context
from django.template import RequestContext, loader


def menu(request):
    rest_info = RestaurantInfo.objects.first()
    template = loader.get_template('menu.html')
    categories = Category.objects.all()
    context = get_context(request, {
        'restaurant_name': rest_info.name,
        'rest_info': rest_info,
        'categories': categories
    })
    return HttpResponse(template.render(context))

def category(request, category_name):
    selected_category = Category.objects.get(slug=category_name)
    template = loader.get_template('category.html')
    context = get_context(request, {
        'category': selected_category
    })

    return HttpResponse(template.render(context))


def about_us(request):
    about_us = RestaurantInfo.objects.first()
    template = loader.get_template('aboutus.html')
    context = get_context(request, {
        'about_us': about_us
    })

    return HttpResponse(template.render(context))


def locations(request):
    template = loader.get_template('locations.html')
    context = get_context(request, {
    })

    return HttpResponse(template.render(context))
