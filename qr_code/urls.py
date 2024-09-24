from django.urls import path
from .views import generate_QR_code
from .views import register_user
from .views import login_user
from .views import profile_view
urlpatterns = [
    path('', generate_QR_code, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),  # Add URL pattern for the login page
    path('profile/', profile_view, name='profile'),

]