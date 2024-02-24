from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Leader
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    object=Leader.objects.all()
    return  render(request,"index.html",{'result':obj,'res':object})
