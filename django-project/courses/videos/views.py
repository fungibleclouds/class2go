from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader
from c2g.models import Course, Video
from django.template import RequestContext

from c2g.models import Course, Video, VideoActivity
from courses.common_page_data import get_common_page_data
from courses.course_materials import get_course_materials
import datetime
from courses.videos.forms import VideoUploadForm
import gdata.youtube
import gdata.youtube.service

def list(request, course_prefix, course_suffix):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    if 'id' in request.GET:
        #process Video model instance with this youtube id
        #and other stuff
        video = Video.objects.get(pk=request.GET['vid'])
        video.url = request.GET['id']
        video.save()
        video.create_production_instance()
        print "WADIDOD"

    section_structures = get_course_materials(common_page_data=common_page_data, get_video_content=True, get_pset_content=False)
    
    return render_to_response('videos/'+common_page_data['course_mode']+'/list.html', {'common_page_data': common_page_data, 'section_structures':section_structures}, context_instance=RequestContext(request))
    
def view(request, course_prefix, course_suffix, slug):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404
    
    video = None
    video_rec = None
    if request.user.is_authenticated():
        video = Video.objects.get(course=common_page_data['production_course'], slug=slug)
        #video_rec = request.user.videoactivity_set.filter(video=video)
        video_rec = request.user.videoactivity_set.filter(video=video)

    return render_to_response('videos/view.html', {'common_page_data': common_page_data, 'video': video, 'video_rec':video_rec}, context_instance=RequestContext(request))
    
def edit(request, course_prefix, course_suffix, video_id):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404
        
    return render_to_response('videos/edit.html', 
            {'request': request,
             'course_prefix': course_prefix,
             'course_suffix': course_suffix,
             'course': course,
             'video_id': video_id,
             },
            context_instance=RequestContext(request))

def GetAuthSubUrl(request):
    next = "http://localhost:8000" + request.path
    scope = 'http://gdata.youtube.com'
    secure = False
    session = True

    yt_service = gdata.youtube.service.YouTubeService()
    return yt_service.GenerateAuthSubURL(next, scope, secure, session)

def upload(request, course_prefix, course_suffix):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404

    data = {'common_page_data': common_page_data}

    if 'token' in request.GET:
        token = request.GET['token']
        data['token'] = token

        yt_service = gdata.youtube.service.YouTubeService()
        #yt_service.developer_key = 'AI39si5GlWcy9S4eVFtajbVZk-DjFEhlM4Zt7CYzJG3f2bwIpsBSaGd8SCWts6V5lbqBHJYXAn73-8emsZg5zWt4EUlJJ4rpQA'
        #yt_service.SetAuthSubToken(token)
        #yt_service.UpgradeToSessionToken()

        yt_logged_in = True
        form = VideoUploadForm(course=common_page_data['course'])
        data['form'] = form
    else:
        # user is not logged into google account for youtube
        yt_logged_in = False
        authSubUrl = GetAuthSubUrl(request)
        data['authSubUrl'] = authSubUrl

    data['yt_logged_in'] = yt_logged_in
    return render_to_response('videos/upload.html',
                              data,
                              context_instance=RequestContext(request))
