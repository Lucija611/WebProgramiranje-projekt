from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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


@login_required
def dashboard(request):
    my_notes = request.user.note_set.all().order_by('-created_at')
    favorite_notes = request.user.favorite_notes.all().order_by('-created_at')

    for note in my_notes:
        note.is_fav = note.is_favorited_by(request.user)

    for note in favorite_notes:
        note.is_fav = note.is_favorited_by(request.user)

    context = {
        'my_notes': my_notes,
        'favorite_notes': favorite_notes,
    }
    return render(request, 'accounts/dashboard.html', context)