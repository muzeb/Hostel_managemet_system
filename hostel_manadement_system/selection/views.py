from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse, Http404
# Create your views here.


def home(request):
    return render(request, 'home.html')


def start(request):
    return render(request, 'start.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            Student.objects.create(user=new_user)
            cd = form.cleaned_data
            print(str(cd))
            user = authenticate(
                request,
                username=cd['username']
            )

