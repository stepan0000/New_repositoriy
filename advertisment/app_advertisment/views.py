from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Advertisment
from .forms import AdvertismentForm
from django.urls import reverse
# Create your views here.
def index(request):
    advertisement = Advertisment.objects.all()
    context = {'advertisement':advertisement}
    return render(request,'index.html',context=context)

def top(request):
    return render(request,'top-sellers.html')


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertismentForm(request.POST,request.FILES)
        if form.is_valid():
            advertisement = Advertisment(**form.changed_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('/')
            return redirect(url)
    else:
        form = AdvertismentForm()
    context = {'form':form}
    return render(request,'advertisement-post.html',context=context)


def advertisement(request):
    return render(request,'advertisement.html')

def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def register(request):
    return render(request,'register.html')