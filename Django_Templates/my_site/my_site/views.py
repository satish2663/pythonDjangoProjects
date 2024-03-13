from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("HOME VIEW")

def custom_view(request,exception):
    return render(request,'errorCustom.html',status=404)