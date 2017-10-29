from django.views.generic import View
from django.shortcuts import render

# Create your views here.


class IndexView(View):
    url = '/'
    template_for_users = 'charges/index.html'
    template_for_strangers = 'charges/loginsys.html'


    def get(self, request, context=None):
        if request.user.is_authenticated():
            return render(request, self.template_for_users, context)
        else:
            return render(request, self.template_for_strangers, context)