from django.shortcuts import render, redirect
from django.views.generic import View, FormView, RedirectView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserForm
import re

# Create your views here.


class RegisterView(FormView):
    url = '/auth/register/'
    template_name = 'users/register.html'
    form_class = UserForm


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


    def get_context_data(self, **kwargs):
        context = {
            'form': UserForm(),
            'message': kwargs.get('message'),
        }

        return context


    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if User.objects.filter(username=email).exists():
            return self.error('User with email exists.')

        if password != confirm_password:
            return self.error('Passwords don\'t match.')

        if not self.password_validation(password):
            return self.error('Invalid password.')

        user = form.save(commit=False)
        user.email = ''
        user.username = email
        user.set_password(password)
        user.is_active = False
        user.save()

        send_mail('Theme', 'Test message', settings.EMAIL_HOST_USER, ['alexei03091997@gmail.com',])

        return redirect('/')


    def password_validation(self, password):
        return bool(re.match(r'^[\d|a-zA-Z]{8,}$', password))


    def error(self, msg):
        context = self.get_context_data(message=msg)
        return render(self.request, self.template_name, context)


    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated():
            return redirect('/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class LoginView(View):
    success_url = '/'
    url = '/auth/login/'
    template_name = 'users/login.html'


    def get(self, request, context=None):
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(self.success_url)
            else:
                context = {'message': 'Your account is deactivated.'}
                return self.get(request, context)
        else:
            context = {'message': 'Invalid data.'}
            return self.get(request, context)


    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated():
            return redirect(self.success_url)

        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


def register_success(request):
    return HttpResponse('register success')
