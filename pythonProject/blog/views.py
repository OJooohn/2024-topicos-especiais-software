from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    return HttpResponse('Pagina do blog')

def ti(request):
    return HttpResponse('Pagina de ti')