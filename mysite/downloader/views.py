
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


def index(request): 
    return render(request, "homepage.html")
    #  return HttpResponse("Hello world, you're at my illegal website. ")

def submit_link(request): 
    print("hello world")
    if request.method == 'GET': 
        fout = open("hai.txt", "w")
        #  ytLink = request.GET["text"]
        ytLink = request.GET["url_input"]
        fout.write(ytLink)
        fout.close()
        return render(request, "homepage.html")

