from django.shortcut import render
from django.http  import HttpResponse 
from first_app.models import Musician,Album


def index(request):
    diction = {}
    return render(request,'first_app/index.html',context=diction)