from django.http import HttpResponse
from courses import views


def index(request):
    return HttpResponse("Courses App")


