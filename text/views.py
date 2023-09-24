from django.shortcuts import render


# Create your views here.

def text_analyzer(request):
    if request.method == 'POST':
        pass
        
    return render(request,'index.html')

