from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from notes.models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                faculty=form.cleaned_data['faculty']
            )
            login(request, user)
            return redirect('notes:home')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})