from django.shortcuts import render

# Create your views here.

def index(request):

    text = {'title': "hola", 'read': "aqui programando con django"}
    
    return render(request, 'base.html', {'text': text})