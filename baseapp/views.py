from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.ml.sentiment_model import analyze_sentiment
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
    user_profile = user.profile
    address = user.address

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile, user=user, address=address)
        if form.is_valid():
            # Save user data
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone = form.cleaned_data['phone']
            user.save()

            # Save user address data
            address.home = form.cleaned_data['home']
            address.save()

            # Save profile data
            form.save()

            messages.success(request, f'Профиль {user} обновлен!')

            return redirect('profile')
        else:
            messages.error(request, 'Ошибка заполнения профиля. Проверьте введённые данные.')
    else:
        form = ProfileForm(instance=user_profile, user=user)

    return render(request, 'profile/index.html', {'form': form})
