from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    context={}
    form = UserCreationForm(request.POST or None)
    return render(request, 'register/signup.html', context)
