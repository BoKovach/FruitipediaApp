from django import forms

from FruitipediaApp.profile_app.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image_url', 'age']
