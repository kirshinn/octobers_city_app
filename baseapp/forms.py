from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser, Address


class CustomUserCreationForm(UserCreationForm):
    # Поля для модели Address
    home = forms.IntegerField(required=True, label='Номер дома')
    apartment = forms.IntegerField(required=True, label='Номер квартиры')

    class Meta:
        model = CustomUser
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
        self.fields['home'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': 'Номер дома',
        })
        self.fields['apartment'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': 'Номер квартиры',
        })

        # Убираем help_text
        for field in self.fields:
            self.fields[field].help_text = ''

    def save(self, commit=True):
        # Сначала сохраняем CustomUser
        user = super().save(commit=False)
        if commit:
            user.save()

        # Создаем или обновляем связанный Address
        address_data = {
            'home': self.cleaned_data.get('home'),
            'apartment': self.cleaned_data.get('apartment'),
        }

        # Проверяем, есть ли уже адрес у пользователя
        address, created = Address.objects.get_or_create(user=user, defaults=address_data)
        if not created:
            # Если адрес уже существует, обновляем его
            for key, value in address_data.items():
                setattr(address, key, value)
            address.save()

        return user
