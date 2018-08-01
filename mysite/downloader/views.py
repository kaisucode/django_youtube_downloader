
from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request): 
    return HttpResponse("Hello world, you're at my illegal website. ")

def submit_link(request): 
    print("hello world")
    if request.method == 'GET': 
        fout = open("hai.txt", "w")
        ytLink = request.GET["text"]
        fout.write(ytLink)
        fout.close()
        return render(request, TemplateView.as_view(template_name='homepage.html/'))

