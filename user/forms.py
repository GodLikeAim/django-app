from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput)

# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanici Adi")
    password = forms.CharField(max_length=50, label="Sifre", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50, label="Sifre Dogrulama", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Sifreler eslesmiyor.")
        values = {
            "username": username,
            "password": password
        }
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu kullanıcı adı zaten kullanılıyor.")
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return values

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Şifre",
        required=True,  # Boş geçilemez
        help_text="Your password must contain at least 8 characters and must not be too similar to your other personal information."
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        label="Şifre Doğrulama",
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Kullanıcı adını readonly yap
        self.fields['username'].widget.attrs['readonly'] = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password is required")
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
