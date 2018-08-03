
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings

from wsgiref.util import FileWrapper



import os
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

        #  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #      result = ydl.extract_info(ytLink, download=True)

        #  filePath = settings.BASE_DIR + "/mp3/" + result.get("title", None)+".mp3"
        filePath = settings.BASE_DIR + "/mp3/test.mp3"


        contents = open(filePath, "rb")
        wrapper = FileWrapper( contents )

        response = HttpResponse(wrapper, content_type = "audio/mpeg")
        response['Content-Length'] = os.path.getsize( filePath ) # not FileField instance
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename( filePath )
        return response



        #  return render(request, "homepage.html", {"displayErrorVar": False, "shouldPauseEnter": "false", "song_url": songFilename})
    except Exception as e:
        print(e)
        print("exception")
        return render(request, "homepage.html", {'displayErrorVar': True, "shouldPauseEnter": "true"})

