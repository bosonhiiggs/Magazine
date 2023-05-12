from django import forms

from myauth.models import Profile


class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'avatar',