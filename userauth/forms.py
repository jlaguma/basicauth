from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms


class RegistrationForm(UserCreationForm):
    """Custom Registration form."""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')


class LoginForm(AuthenticationForm):
    """Custom Login form."""
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class EditProfileForm(UserChangeForm):
    """Custom Edit Profile form."""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ChangePasswordForm(PasswordChangeForm):
    """Custom Change Password form."""
    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')