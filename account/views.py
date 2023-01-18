from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm

def register_user(request):

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(to='account:login')
        return HttpResponse("Invalid form")

    form = RegisterForm()
    context = {
        'form':form
    }
    return render(request, 'account/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['passowd']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect(to='main:index')
            return HttpResponse('Not found this user')
        return HttpResponse("Invalid form")
    form = LoginForm
    context = {
        "form":form
    }
    return render(request, 'account/login.html', context)

def logout_user(request):
    logout(request)
    return redirect(to='account:login')


