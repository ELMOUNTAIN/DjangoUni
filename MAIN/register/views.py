from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm

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

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                return redirect("home")
    context.update({
        "form":form,
        "title": "signin",
    })
    return render(request, "register/signin.html", context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("home")
        
    context.update({
        "form":form,
        "title": "signin",
    })   

    return render(request, "register/update.html", context)
