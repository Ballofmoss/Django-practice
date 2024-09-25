from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from account.models.profile import Gender, Profile



class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите логин',
            }
        ),
        required=False,
        validators=[RegexValidator(r'[^0-9а-яА-ЯёЁ]', "Введите логин латиницей")],
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
        attrs={
            'autocomplete': 'email',
            'placeholder': 'Введите электронную почту',
            }
        ),
        required=False
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль',
            }
        ),
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль',
            }
        ),
        required=False
    )
    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Введите электронную почту', code='invalid')
        return email

        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Логин',
            }
        ),
        required=False
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Пароль'
            }
        ),
        required=False
    )
    
    error_messages = {
        "invalid_login": (
            "Введите логин и пароль правильно"
        ),
    }
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('Такого пользователя не существует', code='invalid')
        return username
    
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField( max_length=100, required=False, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите новый логин',
            }
        ))
    email = forms.CharField( max_length=100, required=False, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите новую электронную почту',
            }
        ))
    
    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    gender = forms.ChoiceField( choices=Gender, required=False)
    
    country = forms.CharField( max_length=100, required=True, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите страну',
            }
        ))
    city = forms.CharField( max_length=100, required=True, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите город',
            }
        ))
    street = forms.CharField( max_length=100, required=True, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите улицу',
            }
        ))
    house = forms.CharField( max_length=20, required=True, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите номер дома',
            }
        ))
    apartament_number = forms.CharField( max_length=100, required=True, widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите номер квартиры',
            }
        ))

    class Meta:
        model = Profile
        fields = ('gender', 'country', 'city', 'street', 'house', 'apartament_number')