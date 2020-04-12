from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=yTO39OFoyt0').streams.first().download()
