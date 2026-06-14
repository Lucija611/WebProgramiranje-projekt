from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note, Review
from .forms import NoteForm, ReviewForm
from .serializers import NoteSerializer


def home(request):
    query = request.GET.get('query', '')

    if query:
        notes = Note.objects.filter(course_name__icontains=query)
    else:
        notes = Note.objects.all()

    notes = notes.order_by('-created_at')

    for note in notes:
        note.is_fav = note.is_favorited_by(request.user)

    context = {
        'notes': notes,
        'query': query,
    }
    return render(request, 'notes/home.html', context)


def literature(request):
    return render(request, 'notes/literature.html')


@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes:home')
    else:
        form = NoteForm()

    context = {
        'form': form,
    }
    return render(request, 'notes/upload_note.html', context)


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    reviews = note.review_set.all().order_by('-created_at')
    review_form = ReviewForm()
    note.is_fav = note.is_favorited_by(request.user)

    context = {
        'note': note,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'notes/note_detail.html', context)


def download_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return FileResponse(note.file.open(), as_attachment=True, filename=note.file.name)


@login_required
def add_review(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.note = note
            review.save()

    return redirect('notes:note_detail', note_id=note.id)


@login_required
def edit_note(request, note_id):
    note = Note.objects.get(pk=note_id)

    if note.author != request.user:
        return redirect('notes:home')

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = NoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'notes/edit_note.html', context)


@login_required
def toggle_favorite(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if note.favorited_by.filter(id=request.user.id).exists():
        note.favorited_by.remove(request.user)
    else:
        note.favorited_by.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'notes:home'))


@login_required
def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)

    if note.author == request.user:
        note.delete()

    return redirect('accounts:dashboard')


# --- API view-ovi (DRF) ---

@api_view(['GET'])
def api_notes(request):
    query = request.GET.get('query', '')

    if query:
        notes = Note.objects.filter(course_name__icontains=query)
    else:
        notes = Note.objects.all()

    notes = notes.order_by('-created_at')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_toggle_favorite(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if not request.user.is_authenticated:
        return Response({'error': 'Morate biti prijavljeni.'}, status=401)

    if note.favorited_by.filter(id=request.user.id).exists():
        note.favorited_by.remove(request.user)
        is_fav = False
    else:
        note.favorited_by.add(request.user)
        is_fav = True

    return Response({'is_fav': is_fav})