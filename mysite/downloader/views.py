
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

import youtube_dl
import time

def index(request): 
    return render(request, "homepage.html")
    #  return HttpResponse("Haii")

def submit_link(request): 
    try:
        ytLink = request.GET["url_input"]

        currentTime = time.strftime("%Y%m%d-%H%M%S")
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': currentTime+'/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(ytLink, download=True)


        return render(request, "homepage.html", {"displayErrorVar": False})
    except Exception as e:
        return render(request, "homepage.html", {'displayErrorVar': True})

