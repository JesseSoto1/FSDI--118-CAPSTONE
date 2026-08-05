from django.urls import path
from django.views.generic import RedirectView
from .views import SignUpView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('signup/', SignUpView.as_view(), name='signup'),
]