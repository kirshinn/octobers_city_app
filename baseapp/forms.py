from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser, Profile, Address


class CustomUserCreationForm(UserCreationForm):
    # Поля для модели Address
    home = forms.IntegerField(required=True, label=_('House number'))
    apartment = forms.IntegerField(required=True, label=_('Apartment number'))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': _('Enter username'),
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': _('Enter email'),
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': _('Enter password'),
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': _('Confirm password'),
        })
        self.fields['home'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': _('House number'),
        })
        self.fields['apartment'].widget.attrs.update({
            'class': 'form-control mt-2',
            'placeholder': _('Apartment number'),
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

class ProfileForm(forms.ModelForm):
    # User
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone = forms.CharField(max_length=17, required=False)
    telegram = forms.CharField(max_length=32, required=False)
    whatsapp = forms.CharField(max_length=14, required=False)

    # Address
    city = forms.CharField(max_length=30, required=False)
    street = forms.CharField(max_length=50, required=False)
    home = forms.IntegerField(max_value=100, required=False)
    entrance = forms.IntegerField(max_value=10, required=False)
    floor = forms.IntegerField(max_value=30, required=False)
    apartment = forms.IntegerField(max_value=500, required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'allow_data_access']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        address = kwargs.pop('address', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['phone'].initial = user.phone
            self.fields['telegram'].initial = user.telegram
            self.fields['whatsapp'].initial = user.whatsapp

        if address:
            self.fields['city'].initial = address.city
            self.fields['street'].initial = address.street
            self.fields['home'].initial = address.home
            self.fields['entrance'].initial = address.entrance
            self.fields['floor'].initial = address.floor
            self.fields['apartment'].initial = address.apartment
