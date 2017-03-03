from django.shortcuts import render
from feedme.models import *
from .forms import TitleForm
# Create your views here.


def show_all_videos(request):
    videos = video.objects.all()
    return render(request, 'all_videos.html', {'videos':videos})


def filter_test(request):

    if request.method == 'POST':
        form = TitleForm(request.POST)
        # kwargs = dict(request.POST)
        kwargs = {x:request.POST.get(x) for x in request.POST.keys()}
        # kwargs = {'title__icontains':'Blanditiis'}
        videos = video.objects.filter(**kwargs)

    else:
        form = TitleForm()
        videos = video.objects.all()
        kwargs = {}

    vars = {'videos':videos, 'form': form, 'kwargs' : kwargs}


    return render(request, 'all_videos.html', vars)


