from django.shortcuts import render, redirect
from django.views.generic import View, RedirectView, FormView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
from .validators import *
import json
import re

# Create your views here.


class AuthView(View):
    template_name = 'users/loginsys.html'


    def get(self, request):
        context = {'form': RegisterForm()}
        return render(request, self.template_name, context)


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


class RegisterView(FormView):
    url = '/auth/register/'
    form_class = RegisterForm
    template_name = 'users/loginsys.html'


    def get(self, request, *args, **kwargs):
        return redirect('/')


    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)


    '''def validation(self):
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
    '''


    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
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


class RegisterValidation(FormView):
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        return redirect('/')


    def form_invalid(self, form):
        print(form.cleaned_data)
        errors = json.loads(form.errors.as_json())
        errors = self.filter_errors(errors)

        response = {'message': ''}

        if 'username' in errors.keys():
            response['message'] = errors['username']
        elif 'first_name' in errors.keys():
            response['message'] = errors['first_name']
        elif 'password' in errors.keys():
            response['message'] = errors['password']
        elif 'cpsw' in errors.keys():
            response['message'] = errors['cpsw']

        response['fields'] = list(errors.keys())
        return JsonResponse(json.dumps(response), safe=False)


    def filter_errors(self, data):
        errors = {}

        for k, v in data.items():
            if v[0]['code'] != 'required':
                if k == '__all__':
                    k = 'cpsw'

                errors[k] = v[0]['message']

        return errors


    def form_valid(self, form):
        return redirect('/auth/register/')