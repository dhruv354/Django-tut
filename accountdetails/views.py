from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = User.objects.create_user(username=name, password=password, email=email)
        user.save()
        print('user created')

        return redirect('/')
    else:
        return render(request, 'register.html')
