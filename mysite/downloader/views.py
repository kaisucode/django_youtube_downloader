
from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello world, you're at my illegal website. ")

