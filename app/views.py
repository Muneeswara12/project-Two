from django.shortcuts import render

# Create your views her
def first(request):
    return render(request,'new.html')