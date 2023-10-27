from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket

from django.contrib import auth, messages
from django.urls import reverse


# Вход пользователя в систему
def login(request):
    # GET запрос - отображение страницы
    if request.method == 'GET':
        context = {'form': UserLoginForm()}
        return render(request, 'user/login.html', context)
    # POST запрос - отправка данных
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        # Для валидации данных (аудит)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            # Проводим аунтефикацию с бд
            user = auth.authenticate(request,username = username , password = password)

            # Если пользователь существует - авторизовываем
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('home'))
        # Если пользователь не существует - отправляем ошибку
        else:
                context = {'form': UserLoginForm()}
                return render(request, 'user/notlogin.html', context)
    
       
# Регистрация пользователя
def registration(request):
    # GET запрос - отображение страницы
    if request.method == 'GET':
        context = {'form': UserRegistrationForm()}
        return render(request, 'user/registration.html', context)
    
    # POST запрос - отправка данных
    if request.method == 'POST':
         form = UserRegistrationForm(data=request.POST)

         # Сохранение пользователя
         if form.is_valid():
              form.save()
              messages.success(request,'Поздравляем, вы успешно зарегистрировались!')
              return HttpResponseRedirect(reverse('user:login'))
         # Отображение ошибки
         else:
              context = {'form': UserRegistrationForm()}
              return render(request,'user/notregistration.html', context)

# Редактирование данных пользователя
@login_required
def profile(request):
        # GET запрос - отображение страницы
        if request.method == 'GET':
            baskets = Basket.objects.filter(user=request.user)
            context = {
                'title': 'Store - Профиль',
                'form': UserProfileForm(instance=request.user),
                'baskets': baskets,
            }
            return render(request, 'user/profile.html', context)
        # POST запрос - отправка данных
        if request.method == 'POST':
             form = UserProfileForm(instance=request.user, data=request.POST, files = request.FILES) # instance - для пользователя который уже вошел, files - для работы с изображениями
             if form.is_valid():
                  form.save()
                  return HttpResponseRedirect(reverse('user:profile'))
             # Отображение ошибки
             else:
                context = {'form': UserProfileForm(instance=request.user)}
                return render(request,'user/notprofile.html', context)
             
# Выход пользователя из системы        
def logout(request):
     auth.logout(request)
     return HttpResponseRedirect(reverse('home'))

