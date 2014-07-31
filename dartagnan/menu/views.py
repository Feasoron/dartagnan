from django.http import HttpResponse


def index(request):
    return HttpResponse("You have reached the main page for D'Artagnan Hosting. This is the menu view.")