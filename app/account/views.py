from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User

class UserRegisterView(CreateView):
    template_name = 'register.django'
    form_class = UserCreationForm
    model = User
    
class UserLoginView(LoginView):
    template_name = 'login.django'
    form_class = AuthenticationForm
    model = User
    
class UserChangePasswordView(PasswordChangeView):
    template_name = 'change-password.django'
    form_class = PasswordChangeForm
    model = User