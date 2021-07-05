from django import forms

from exam.profiles.models import ProfilesModel


class ProfilesForm(forms.ModelForm):
    class Meta:
        model = ProfilesModel
        fields = '__all__'
        labels = {
            "image_url": "Link to Profile Image"
        }