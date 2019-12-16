from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from .models import Album,Song


def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    context={'all_albums':all_albums}
    '''html=""
    for album in all_albums:
        url=str(album.id)+'/'
        html+='<a href="'+url+'">'+album.album_title+'</a><br>'''
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html',{'all_albums':all_albums})

def detail(request, album_id):
    #return HttpResponse("<h2> Details for Album id:"+str(album_id)+"</h2>")
    try:
        albums=Album.objects.get(pk=album_id)
        all_songs=albums.song_set.all()
        all_songs = list(all_songs)
        all_albums=Album.objects.all()
        songs=Song.objects.all()
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/details.html',{'songs':songs ,'all_albums':all_albums, 'albums':albums ,'all_songs':all_songs})

def favorite(request, album_id):
    return HttpResponse("hello")

# Create your views here.
