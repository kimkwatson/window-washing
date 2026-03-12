from django.http import HttpResponse

def home(request):
    return HttpResponse("Window Washing Service App")
