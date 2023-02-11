from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from team.models import Team


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            return redirect('/log-in/')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form

    })

@login_required
def my_account(request):
    team = Team.objects.filter(created_by= request.user)[0]
    return render(request, 'userprofile/myaccount.html',{
        'team': team
    })