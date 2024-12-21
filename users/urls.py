from django.urls import path
from .views import home, profile, RegisterView, contact_view, dashboard

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('contact/', contact_view, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
]
