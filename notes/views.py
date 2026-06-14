from django.shortcuts import render
from .models import Note


def home(request):
    notes = Note.objects.all().order_by('-created_at')
    context = {
        'notes': notes,
    }
    return render(request, 'notes/home.html', context)


def literature(request):
    return render(request, 'notes/literature.html')


def upload_note(request):
    return render(request, 'notes/upload_note.html')


def note_detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    context = {
        'note': note,
    }
    return render(request, 'notes/note_detail.html', context)