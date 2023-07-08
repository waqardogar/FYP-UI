from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.http import HttpResponse
import json
from . models import video
import cv2 as cv
import numpy as np
import os
# Create your views here.
from django.urls import reverse
import requests
def dashboard(request):
    return render (request,"videostraem/video.html")
def VideoUpload(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        area_name = request.POST.get('area-name')
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'videos'))
        print("FS->",fs)
        filename = fs.save(video_file.name, video_file)
        video_path = fs.url(filename)
        Video = video(AreaName = area_name , file_name = filename , file_path = video_path)
        Video.save()
        def frame_extractor(path,save_dir,current_frame,gap=50):
            temp=1
            vid = cv.VideoCapture(path)
            while True:
                flag , frame = vid.read()
                if flag==False:
                    vid.release()
                    break
                else:
                    if(current_frame%gap==0):
                        cv.imwrite(f"{save_dir}/{temp}.png",frame)
                        temp+=1
                current_frame+=1
        
        current_frame = 0
        path='.'+video_path+"/videos"
        segments = path.split('/')  # Split the path into segments
        new_segments = [segments[0],  segments[1],segments[-1],segments[2]]  # Rearrange the segments
        new_path = '/'.join(new_segments)
        save_dir = os.path.join(settings.MEDIA_ROOT, 'dataset/'+area_name)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            save_dir = os.path.join(settings.MEDIA_ROOT, 'dataset/'+area_name)
        frame_extractor(new_path, save_dir, current_frame,gap=50)
        return render(request,"googlemaps/map.html",{'success': True})
    return render(request,"googlemaps/map.html",{'success': 2})