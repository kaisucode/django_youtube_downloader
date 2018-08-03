
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings


import youtube_dl

def index(request): 
    return render(request, "homepage.html")
    #  return HttpResponse("Haii")

def submit_link(request): 
    try:
        ytLink = request.GET["url_input"]

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': 'mp3/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(ytLink, download=True)
        #  songFilename = settings.BASE_DIR + "/mp3/" + result.get("title", None)+".mp3"
        songFilename = settings.BASE_DIR + "/mp3/test.mp3"

        return render(request, "homepage.html", {"displayErrorVar": False, "shouldPauseEnter": "false", "song_url": songFilename})
    except Exception as e:
        print(e)
        print("exception")
        return render(request, "homepage.html", {'displayErrorVar': True, "shouldPauseEnter": "true"})

