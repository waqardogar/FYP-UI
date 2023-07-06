from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.http import HttpResponse
import json
from . models import video
# Create your views here.
def dashboard(request):
    return render (request,"videostraem/video.html")
def VideoUpload(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        area_name = request.POST.get('area-name')
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'videos'))
        filename = fs.save(video_file.name, video_file)
        video_path = fs.url(filename)
        Video = video(AreaName = area_name , file_name = filename , file_path = video_path)
        Video.save()
        return render(request,"googlemaps/map.html",{'success': True})
    return render(request,"googlemaps/map.html",{'success': 2})