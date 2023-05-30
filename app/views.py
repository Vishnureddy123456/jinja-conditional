from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20}
    return render(request,'condition1.html',context=d)
def conditions(request):
    d={'a':30,'b':20}
    return render(request,'condition2.html',context=d)
