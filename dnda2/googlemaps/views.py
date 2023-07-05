from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.http import HttpResponse
import json
# Create your views here.
def dashboard(request):
    return render (request,"videostraem/video.html")
def VideoUpload(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        
        # Save the video to a folder on the server
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'videos'))
        filename = fs.save(video_file.name, video_file)
        video_path = fs.url(filename)  # Get the path to the saved video
        message = {'success': True, 'message': 'Video uploaded successfully.'}
        
        return render(request,"map.html",{'success': True})
    return render(request,"map.html",{'success': False})
    
    
        # Video.objects.create(path=video_path)