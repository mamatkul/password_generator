from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator_app/home.html')


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('qwertyuiopasdfghjklzxcvbnm'.upper()))

    if request.GET.get('special'):
        characters.extend(list('!"№;%:?*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator_app/password.html', {'password': thepassword})


def about(request):
    mamatkul = 'Simple password generator'
    return render(request, 'generator_app/about.html', {'about': mamatkul})
