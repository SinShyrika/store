from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from user.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from user.models import EmailVerification, User


# Вход пользователя в систему
class UserLoginView(TitleMixin,LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'
# def login(request):
#     # GET запрос - отображение страницы
#     if request.method == 'GET':
#         context = {'form': UserLoginForm(),'title': 'Store - Авторизация'}
#         return render(request, 'user/login.html', context)
#     # POST запрос - отправка данных
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#
#         # Для валидации данных (аудит)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#
#             # Проводим аунтефикацию с бд
#             user = auth.authenticate(request,username = username , password = password)
#
#             # Если пользователь существует - авторизовываем
#             if user is not None:
#                 auth.login(request,user)
#                 return HttpResponseRedirect(reverse('home'))
#         # Если пользователь не существует - отправляем ошибку
#         else:
#                 context = {'form': UserLoginForm()}
#                 return render(request, 'user/notlogin.html', context)

# Регистрация пользователя
class UserRegistrationView(TitleMixin,SuccessMessageMixin,CreateView):
    model = User
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')
    success_message = 'Поздравляем, вы успешно зарегистрировались!'
    title = 'Store - Регистрация пользователя'

# def registration(request):
#     # GET запрос - отображение страницы
#     if request.method == 'GET':
#         context = {'form': UserRegistrationForm()}
#         return render(request, 'user/registration.html', context)
#
#     # POST запрос - отправка данных
#     if request.method == 'POST':
#          form = UserRegistrationForm(data=request.POST)
#
#          # Сохранение пользователя
#          if form.is_valid():
#               form.save()
#               messages.success(request,'Поздравляем, вы успешно зарегистрировались!')
#               return HttpResponseRedirect(reverse('user:login'))
#          # Отображение ошибки
#          else:
#               context = {'form': UserRegistrationForm()}
#               return render(request,'user/notregistration.html', context)

# Редактирование данных пользователя
class UserProfileView(TitleMixin,UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    title = 'Store - Редактирование данных пользователя'

    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user = self.object)
    #     return context

    def get_success_url(self):
        return reverse_lazy('user:profile', args = (self.object.id,))
# @login_required
# def profile(request):
#         # GET запрос - отображение страницы
#         if request.method == 'GET':
#             baskets = Basket.objects.filter(user=request.user)
#             context = {
#                 'title': 'Store - Профиль',
#                 'form': UserProfileForm(instance=request.user),
#                 'baskets': baskets,
#             }
#             return render(request, 'user/profile.html', context)
#         # POST запрос - отправка данных
#         if request.method == 'POST':
#              form = UserProfileForm(instance=request.user, data=request.POST, files = request.FILES) # instance - для пользователя который уже вошел, files - для работы с изображениями
#              if form.is_valid():
#                   form.save()
#                   return HttpResponseRedirect(reverse('user:profile'))
#              # Отображение ошибки
#              else:
#                 context = {'form': UserProfileForm(instance=request.user)}
#                 return render(request,'user/notprofile.html', context)
#
# Выход пользователя из системы        
def logout(request):
     auth.logout(request)
     return HttpResponseRedirect(reverse('home'))


class EmailVerificationView(TitleMixin,TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'user/email_verification.html'

    def get(self,request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))


