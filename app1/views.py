from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    s={'name':'yeswanth'}
    return render(request,'hello.html',s)
