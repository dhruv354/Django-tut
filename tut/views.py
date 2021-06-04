from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def add(request):
    print('printing request object')
    # print(type(request))
    num1 = int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    output = num1 + num2
    return render(request, 'add.html', {'result': output})
