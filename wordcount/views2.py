from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
from pprint import pprint

def kk (request) :
    return HttpResponse("ZBY MANGA")

def home22 (request) :
    return render(request,'homie.html')

def cc (request) :
    ff = request.GET['zby']
    # print(ff)
    hh=ff.split()
    zz=len(hh)
    x = Counter(hh)



    return render(request,'countie.html',{'ww':ff,"zz":zz,"x":x.items()})

def gg (request) :
    return render(request,"aboout.html")