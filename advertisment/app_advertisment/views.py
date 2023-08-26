
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Advertisment

from .forms import AdvertismentForm
from django.urls import reverse
# Create your views here.
def index(request):
    advertisement = Advertisment.objects.all()
    context = {'advertisement':advertisement}
    return render(request,'advertisments/index.html',context=context)

def top(request):
    return render(request,'advertisments/top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertismentForm(request.POST,request.FILES)
        if form.is_valid():
            advertisement = Advertisment( **form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('/')
            return redirect(url)
    else:
        form = AdvertismentForm()
    context = {'form':form}
    return render(request,'advertisments/advertisement-post.html',context=context)


def advertisement(request):
    return render(request,'advertisments/advertisement.html')






