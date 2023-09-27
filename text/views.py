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
        
        new_text = text.replace('\n ','\n\n')
        new_text1 = new_text.replace('\n\r','\n\n')
        print(new_text1)
        paragraphcount = new_text1.split('\n\n')
        print(paragraphcount)
        print(len(paragraphcount))


        context = {
            'status' : True,
            'word_count' : word_count,
            'text' : text,
            'para' : len(paragraphcount)
        }
    return render(request,'index.html',context)

