from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'label': 'Username',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'Username',
            'max_length': '16',
            'min_length': '5',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-input',
            'placeholder': 'youremail@email.com',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-input',
            'placeholder': 'Password',
            'max_length': '22',
            'min_length': '8',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-input',
            'placeholder': 'Confirm Password',
            'max_length': '22',
            'min_length': '8',
        })
        
        
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(
            attrs= {
                'placeholder' : 'Username',
            }
        )
    )
    
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs= {
                'placeholder' : 'Password'
            }
        )
    )