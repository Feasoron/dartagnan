from django.http import HttpResponse
from dartagnan.menu.models import Category
from dartagnan.menu.helpers import get_context
from django.template import RequestContext, loader


def index(request):
    return HttpResponse("You have reached the main page for D'Artagnan Hosting. This is the menu view.")


def category(request, category_name):
    selected_category = Category.objects.get(title=category_name)
    template = loader.get_template('category.html')
    context = get_context(request, {
        'category': selected_category
    })
    return HttpResponse(template.render(context))