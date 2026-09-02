from django.urls import path
from django.views.generic import RedirectView
from .views import SignUpView, ProfileDetailView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
]