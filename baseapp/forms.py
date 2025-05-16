from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': 'Введите имя пользователя',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': 'Введите пароль',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': 'Подтвердите пароль',
        })
        # Убираем help_text
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
