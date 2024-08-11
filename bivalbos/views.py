from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola mundo')
    
def test(request):
    return render(request,'paginas/test.html')
def formas(request):
    return render(request,'formas/index.html')
# Create your views here.
