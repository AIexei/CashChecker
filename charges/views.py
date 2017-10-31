from django.shortcuts import render
from django.views.generic import View

from users.views import AuthView


# Create your views here.


class IndexView(View):
    url = '/'
    template_name = 'charges/index.html'


    def get(self, request):
        if request.user.is_authenticated():
            return render(request, self.template_name)
        else:
            return AuthView().get(request)