# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Album,song
from django.template import loader
from django.shortcuts import render,redirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm




class Indexview(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

class Detailview(generic.DetailView):
    model=Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class songCreate(CreateView):

    model = song
    fields = ['album','file_type', 'song_title']

class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):

        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
             login(request,user)
             return redirect('music:index')

        return render(request, self.template_name, {'form': form})


# def index(request):
#     all_album = Album.objects.all()
#     template=loader.get_template('music/index.html')
#
#     context={
#         'all_album':all_album,
#     }
#     return HttpResponse(template.render(context,request))


# def index(request):
#     all_album=Album.objects.all()
#     html=''
#     for album in all_album:
#         url='/music/'+str(album.id)+'/'
#         html+="<a href='"+url+"'>"+album.album_title+"</a></br>"
#     return HttpResponse(html)


# def detail(request,album_id):
#     try:
#         album = Album.objects.get(id=album_id)
#
#     except Album.DoesNotExist:
#         raise Http404("The requested album does not exist")
#     return render(request, 'music/detail.html', {'album': album })

def favourite(request,album_id):

    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(id = request.POST['song'])
    except:
        return render(request, 'music/detail.html', {'album': album, 'error_message': "select a valid song"})
    else:
     if request.POST['submit']=="favourite":
        selected_song.is_favourite=True
     else:
        selected_song.is_favourite = False
    selected_song.save()
    return render(request, 'music/detail.html', {'album': album})






