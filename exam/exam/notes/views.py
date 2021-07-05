from django.shortcuts import render, redirect

from exam.notes.forms import NotesForm, DeleteNote
from exam.notes.models import NotesModel
from exam.profiles.forms import ProfilesForm
from exam.profiles.models import ProfilesModel


def home(request):
    profile = ProfilesModel.objects.first()
    if not profile:
        if request.method == 'POST':
            form = ProfilesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ProfilesForm()
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)
    else:
        notes = NotesModel.objects.all()
        context = {
            'notes': notes
        }
        return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        note = NotesForm(request.POST)
        if note.is_valid():
            note.save()
            return redirect('home')
        else:
            context = {'note': note}
            return render(request, 'note-create.html', context)
    else:
        note = NotesForm()
        context = {
            'note': note
        }
        return render(request, 'note-create.html', context)


def edit_note(request, pk):
    selected_note = NotesModel.objects.get(pk=pk)
    if request.method == 'POST':
        note = NotesForm(request.POST, instance=selected_note)
        if note.is_valid():
            note.save()
            return redirect('home')
        else:
            context = {'note': note}
            return render(request, 'note-edit.html', context)
    else:
        note = NotesForm(instance=selected_note)
        context = {
            'note': note
        }
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    selected_note = NotesModel.objects.get(pk=pk)
    if request.method == 'POST':
        selected_note.delete()
        return redirect('home')
    else:
        form = DeleteNote(instance=selected_note)
        context = {'form': form}
        return render(request, 'note-delete.html', context)


def details(request, pk):
    note = NotesModel.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)
