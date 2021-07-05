from django.shortcuts import render, redirect

from exam.notes.models import NotesModel
from exam.profiles.models import ProfilesModel


def profile_home(request):
    profile = ProfilesModel.objects.first()
    notes = NotesModel.objects.all()
    context = {
        'profile': profile,
        'notes': notes
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    selected_profile = ProfilesModel.objects.first()
    notes = NotesModel.objects.all()
    selected_profile.delete()
    notes.delete()
    return redirect('home')
