from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import (
UserCreationForm,UserChangeForm,AuthenticationForm
)

YEARS =[x for x in range(1950,2002)]

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=15,help_text=None)
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=PasswordStrengthInput(),help_text=None)
    password2 = forms.CharField(widget=PasswordStrengthInput(),help_text=None)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = User.objects.get(email=email)
            raise forms.ValidationError(
            _('Email Already Exists'),
            code="Email exists",
            params = {"email":email}
            )
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return User

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(required=False,initial="01-01-1950",
    widget=forms.SelectDateWidget(years=YEARS),
    )

    class Meta:
        model = Profile
        fields = [
        'location',
        'birth_date',
        'gender',
        ]

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        profile.location=self.cleaned_data['location']
        profile.birth_date=self.cleaned_data['birth_date']
        profile.gender=self.cleaned_data['gender']

        if commit:
            profile.save()

        return Profile
