from django.shortcuts import render
import shlex

# Create your views here.

def text_analyzer(request):
    context = {
        'status': False
    }
    if request.method == 'POST':
        text = request.POST.get('text_main')
        word_count = len(shlex.split(text))
        print(word_count)
        context = {
            'status' : True,
            'word_count' : word_count,
            'text' : text
        }
    return render(request,'index.html',context)

