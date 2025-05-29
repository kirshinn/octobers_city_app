from django.shortcuts import render


def video_view(request):
    return render(request, 'video.html', {})

def stream_view(request):
    return render(request, 'stream.html', {})
