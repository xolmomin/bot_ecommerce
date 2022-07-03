from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.forms import SignInForm


class IndexPage(TemplateView):
    template_name = 'apps/index.html'


class SignInPage(LoginView):
    form_class = SignInForm
    success_url = reverse_lazy('index')
    template_name = 'apps/sign-in.html'


class SignUpPage(TemplateView):
    template_name = 'apps/sign_up.html'
