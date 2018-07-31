from __future__ import unicode_literals
import youtube_dl


music_links = []

#  music_links.append("")
music_links.append("https://www.youtube.com/watch?v=iD0ffxoTLX0")


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

#  ydl = youtube_dl.YoutubeDL({})
for link in music_links: 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(link, download=True)
        print(result['title'])
        #  ydl.download([link])





