
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


def index(request): 
    return render(request, "homepage.html")
    #  return HttpResponse("Haii")

def submit_link(request): 
    try:
        ytLink = request.GET["url_input"]
        #  fout = open("hai.txt", "w")
        #  fout.write(ytLink)
        #  fout.close()
        return render(request, "homepage.html", {"displayErrorVar": False})
    except Exception as e:
        return render(request, "homepage.html", {'displayErrorVar': True})

