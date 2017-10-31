from django.shortcuts import render, redirect
from django.views.generic import View, RedirectView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
import re

# Create your views here.


class AuthView(View):
    template_name = 'users/loginsys.html'


    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    url = '/auth/login/'


    def get(self, request):
        return redirect('/')


    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('psw')

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                message = ''
            else:
                message = 'Your account is not activated.'
        else:
            message = 'Invalid data.'

        return HttpResponse(message)


class RegisterView(View):
    url = '/auth/register/'


    def get(self, request):
        return redirect('/')


    def post(self, request, *args, **kwargs):

        return self.validation()


    def validation(self):
        self.data = dict()
        self.data['email'] = self.request.POST.get('email')
        self.data['name'] = self.request.POST.get('name')
        self.data['password'] = self.request.POST.get('psw')
        self.data['confirm_password'] = self.request.POST.get('cpsw')
        if User.objects.filter(username=self.data['email']).exists():
            return HttpResponse('User with this email exists.')

        if self.data['password'] != self.data['confirm_password']:
            return HttpResponse('Passwords don\'t match.')

        if not self.password_validation(self.data['password']):
            return HttpResponse('Password must contain latin letters or numbers.')

        user = User.objects.create_user(username=self.data['email'],
                                        email=None,
                                        password=self.data['password'],
                                        first_name=self.data['name'])

        if settings.EMAIL_CONFIRMATION:
            message = "Hello from CashChecker. Confirm your account. Go to http://localhost:8000/"
            send_mail('CC Registration', message, settings.EMAIL_HOST_USER, ['alexei03091997@gmail.com', ])
            user.is_active = False

        user.save()

        return HttpResponse('/')


    def password_validation(self, password):
        return bool(re.match(r'^[\d|a-zA-Z]{8,30}$', password))


    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated():
            return redirect('/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class AccountActivationView(View):
    def get(self, request, *args, **kwargs):
        pass


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)