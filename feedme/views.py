from django.shortcuts import render
from .models import *
from .forms import TitleForm
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import VideoSerializer


# Create your views here.





public_video= {'is_public': 1}
def show_all_videos(request):
    videos = video.objects.all()
    return render(request, 'all_videos.html', {'videos':videos})


def filter_test(request):

    videos = video.objects.filter(is_public=True)

    if request.method == 'POST':
        form = TitleForm(request.POST)
        kwargs = {x:request.POST.get(x) for x in request.POST.keys() if request.POST.get(x) is not ''}
        kwargs.update(public_video)
        videos = videos.filter(**kwargs)
    else:
        form = TitleForm()
        kwargs = {}
        kwargs.update(public_video)
        videos = videos.filter()

    vars = {'videos':videos, 'form': form, 'kwargs' : kwargs}

    return render(request, 'all_videos.html', vars)


class JSONResponse(HttpResponse):
    """
    returns json data
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def json_all_videos(request):
    if request.method == 'GET':
        videos = video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return  JSONResponse(serializer.data)

