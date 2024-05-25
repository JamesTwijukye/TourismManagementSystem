from django.shortcuts import render

# Create your views here.

def WhenView(request):
    return render(request, 'whenToVisit.html')

def WhyView(request):
    return render(request, 'whyvisit.html')

def BeforeView(request):
   
    return render(request, 'before.html')