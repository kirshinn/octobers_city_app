from django.shortcuts import render
from urllib.parse import urlparse

from octobers_city_app import settings


def video_view(request):
    return render(request, 'video.html', {})


def stream_view(request):
    camera_link = settings.CAMERA_LINKS[0]
    parsed = urlparse(camera_link)
    if parsed.scheme not in ['http', 'https']:
        camera_link = ""
    return render(request, 'stream.html', {'camera_link': camera_link})
