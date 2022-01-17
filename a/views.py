from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from a.form import SignUpform, Student
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission

def home_page(request):
    return render(request, 'home.html')


@login_required
def user_view(request):
    form = SignUpform()
    return render(request, 'user.html', {'form': form})


def logout_view(request):
    return render(request, 'registration/logout.html')


def signup_view(request):
    form = SignUpform()
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'registration/signup.html', context={'form': form})


