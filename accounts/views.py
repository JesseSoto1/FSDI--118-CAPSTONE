from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.



class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'  
    form_class = UserCreationForm # creates objects from a form class
    success_url = reverse_lazy('login')
    success_message = "profile was created successfully"

    