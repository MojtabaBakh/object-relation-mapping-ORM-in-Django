from django.db import models
from django.shortcuts import render
from .models import Student , Package
from django.db.models import Q

# Create your views here.



def index(request): 
    
    data=Student.objects.filter(name = "maryam") 
    # students=Student.objects.filter( name__startswith = "m" )
    # students=Student.objects.filter( description__contains = "this" )
    # data=Student.objects.filter( course__lesson__name='lesson1')
    return render(request , "student/index.html", {"data" : data})

def index2(request):
    # data=Package.objects.filter( course__lesson__name='lesson1' , course__student__name='ali')
    # data=Package.objects.filter( course__lesson__name='lesson1') | Package.objects.filter(course__student__name='maryam')
    # data=Package.objects.filter( Q(course__lesson__name='lesson1') | Q(course__student__name='javad'))
    data=Package.objects.filter( Q(course__lesson__name='lesson1') & (Q(course__student__name='javad') |Q(course__student__name__startswith='m'))  )
    
    
    
    return render(request , "student/index.html", {"data" : data})