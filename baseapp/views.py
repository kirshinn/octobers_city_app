from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.ml.sentiment_model import analyze_sentiment
from accounts.models import Profile, Address
from .forms import CustomUserCreationForm, ProfileForm # Используем кастомную форму для User

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте введённые данные.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def protected(request):
    text = "I love Django!"
    result = analyze_sentiment(text)
    return render(request, 'protected.html', {'text': text, 'result': result})

@login_required
def profile(request):
    user = request.user

    # Проверяем и получаем/создаём профиль
    user_profile, profile_created = Profile.objects.get_or_create(user=user)

    # Проверяем и получаем/создаём адрес
    address, address_created = Address.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile, user=user, address=address)
        if form.is_valid():
            # Save user data
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone = form.cleaned_data['phone']
            user.telegram = form.cleaned_data['telegram']
            user.save()

            # Save user address data
            address.city = form.cleaned_data['city']
            address.street = form.cleaned_data['street']
            address.home = form.cleaned_data['home']
            address.entrance = form.cleaned_data['entrance']
            address.floor = form.cleaned_data['floor']
            address.apartment = form.cleaned_data['apartment']
            address.save()

            # Save profile data
            form.save()

            messages.success(request, f'Профиль {user} обновлен!')

            return redirect('profile')
        else:
            messages.error(request, 'Ошибка заполнения профиля. Проверьте введённые данные.')
            messages.warning(request, form.errors.as_text())
    else:
        form = ProfileForm(instance=user_profile, user=user, address=address)

    return render(request, 'profile/index.html', {'form': form})
