import re
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import (
UserCreationForm,UserChangeForm,AuthenticationForm,PasswordChangeForm
)
from zxcvbn_password import zxcvbn
from zxcvbn_password.widgets import PasswordStrengthInput, PasswordConfirmationInput

YEARS =[x for x in range(1950,2002)]

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="Password",widget=PasswordStrengthInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password",widget=PasswordConfirmationInput(attrs={'placeholder': 'Re-enter Password'},confirm_with='password1'))

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

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        first_name=self.cleaned_data.get('first_name')
        last_name=self.cleaned_data.get('last_name')

        if password1 != password2:
            raise forms.ValidationError("Passwords did not match")

        if len(password1)<8:
            raise forms.ValidationError(
            _('Password should be atleast 8 characters'),
            code="Too Small"
            )
        if password1:
            score = zxcvbn(password1,[first_name,last_name])['score']
            if score < 3:
                raise forms.ValidationError(
                _('Try a Strong Password'),
                code="Too Weak"
                )
        if password1.isdigit():
            raise forms.ValidationError(
            _("Password can't be entirely numeric"),
            code="Numeric"
            )

        return password2

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

    def clean_username(self):
        username = self.cleaned_data['username']
        regex = re.compile('[@_,.\-/\'/\"/+!#$%^&*()<>?/\\\\|}{~:]')
        if username.isdigit():
            raise forms.ValidationError(
            _("Username can't be entirely numeric"),
            code="Numeric"
            )
        if re.match(r"^(?=.{5,15}$)",username)==None:
            if len(u)<5:
                print("less than 5 characters")
                raise forms.ValidationError(
                _("Username less than 5 characters"),
                code="small"
                )
            else:
                raise forms.ValidationError(
                _("Username more than 15 characters"),
                code="large"
                )

        if regex.search(username):
            raise forms.ValidationError(
            _("Username can't contain special characters"),
            code="special characters"
            )

        if username[0].isdigit():
            raise forms.ValidationError(
            _("Username can't start with a number"),
            code="start with a number"
            )
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        regex = re.compile('[@_,.\-/\'/\"/+!#$%^&*()<>?/\\\\|}{~:]')
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError(
            _("First name can't contain a number"),
            code="Numeric"
            )
        if regex.search(first_name):
            raise forms.ValidationError(
            _("First name can't contain special characters"),
            code="special characters"
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        regex = re.compile('[@_,.\-/\'/\"/+!#$%^&*()<>?/\\\\|}{~:]')
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError(
            _("Last name can't contain a number"),
            code="Numeric"
            )
        if regex.search(last_name):
            raise forms.ValidationError(
            _("Last name can't contain special characters"),
            code="special characters"
            )
        return last_name

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return User

class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]

    def clean_new_password2(self):
        password = self.cleaned_data.get('old_password')
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')       

        if password1 != password2:
            raise forms.ValidationError("Passwords did not match")

        if len(password1)<8:
            raise forms.ValidationError(
            _('Password should be atleast 8 characters'),
            code="Too Small"
            )
        if password1:
            score = zxcvbn(password1)['score']
            if score < 3:
                raise forms.ValidationError(
                _('Try a Strong Password'),
                code="Too Weak"
                )
        if password1.isdigit():
            raise forms.ValidationError(
            _("Password can't be entirely numeric"),
            code="Numeric"
            )

        return password2

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
    birth_date = forms.DateField(label="Birth Date",required=False,initial="01-01-1950",
    widget=forms.SelectDateWidget(years=YEARS),
    )
    gender = forms.CharField(label="Gender",required=False,widget=forms.RadioSelect(choices=[('male','Male'),('female','Female')]))
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
