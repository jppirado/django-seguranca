from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView( TemplateView):
    template_name = 'login.html'


class MyProfileView(TemplateView , LoginRequiredMixin):
    template_name = 'perfil.html'
