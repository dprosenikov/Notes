from django import forms

from exam.notes.models import NotesModel


class NotesForm(forms.ModelForm):
    class Meta:
        model = NotesModel
        fields = '__all__'


class DeleteNote(NotesForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'