from django.shortcuts import render
from .models import Image,Location


def pictures(request):
    pics = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'photos.html',{'pics':pics,'locations':locations})