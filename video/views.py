from django.shortcuts import render, redirect, get_object_or_404
from .models import Video

def video_list(request):
    video_list = Video.objects.all()
    return render(request, 'video/video_list.html', {'video_list':video_list})

def video_new(request):
    if request.method == 'POST': # 새로운 비디오 데이터를 업로드할 때
        title = request.POST['title']
        video_key = request.POST['video_key']
        Video.objects.create(title=title, video_key=video_key)
        return redirect('video_list')
    elif request.method == 'GET': # 새로운 비디오를 추가할 템플릿을 가져와야할 때
        return render(request, 'video/video_new.html')

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video/video_detail.html', {'video':video})