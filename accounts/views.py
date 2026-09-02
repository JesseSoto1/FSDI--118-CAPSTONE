from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

# IMPORT your models and forms here
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm  # You need to create these in forms.py

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'  
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    success_message = "Account was created successfully"
    model=User

    def form_valid(self, form): # add form_valid when trying to create Users with Profiles.
        # save the user
        response = super().form_valid(form)
        
        created_user = self.object

        # create a profile for that user
        Profile.objects.create(user=created_user)

        return response



# FIXED: Inherit from DetailView to display model data
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    context_object_name = 'profile'

    # This ensures a user only sees their own profile via request.user
    def get_object(self, queryset=None):
        return self.request.user.profile


# FIXED: Using actual Forms instead of the database Model
@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile') # Adjust this to your profile URL name

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile_update.html', context)
