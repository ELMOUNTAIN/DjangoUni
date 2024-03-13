from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    context={}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save
            login(request, new_user())
            return redirect("home")
    context.update({
        "form":form,
        "title": "Signup",
    })
    return render(request, 'register/signup.html', context)
