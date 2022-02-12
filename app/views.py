import profile
import uuid
from django.shortcuts import render, redirect
from django.views import View
from .models import Profile as Profiless ,Movie
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:profile')
        return render(request,'index.html')

@method_decorator(login_required,name="dispatch")
class Profiles(View):
    def get(self, request, *args, **kwargs):
        profile=request.user.profile.all()
        print(profile)
        return render (request,'profile.html',{'profile':profile})


        
@method_decorator(login_required,name="dispatch")
class ProfileCreate(View):
    def get(self,request,*args,**kwargs):
        form= ProfileForm()
        return render(request,'profileCreate.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            # print(form.cleaned_data)
            profiles = Profiless.objects.create(**form.cleaned_data)
            if profiles:
                request.user.profile.add(profiles)
                return redirect('app:profile')
        return render(request,'profileCreate.html',{'form':form})


@method_decorator(login_required,name="dispatch")
class Watch(View):
    def get(self,request,profile_id,*args,**kwargs):
        try:
            profile=Profiless.objects.get(uuid=profile_id)
            movie = Movie.objects.all()

            if profile not in request.user.profile.all():
                return redirect(to='app:profile')
            return render (request,'movie.html',{'movie':movie})
        except Profiless.DoesNotExist:
            return redirect(to='app:profile')
@method_decorator(login_required,name="dispatch")
class ShowMovieDetails(View):
    def get(self,request,movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            return render(request,'movie_details.html',{'movie':movie})
        except Movie.DoesNotExist:
            return redirect('app:profile')

class ShowMovie(View):
    def get(self,request,movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.video.values()
            return render(request,'movieshow.html',{'movie':list(movie)})
        except Movie.DoesNotExist:
            return redirect('app:profile')