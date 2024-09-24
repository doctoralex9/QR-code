from django.urls import path
from .views import generate_QR_code
from .views import register_user
from .views import login_user
from .views import profile_view
urlpatterns = [
    path('', generate_QR_code, name='home'),
    path('register/', register_user, name='register'),
<<<<<<< HEAD
    path('login/', login_user, name='login'),  # Add URL pattern for the login page
=======
    path('login/', login_user, name='login'),  
>>>>>>> 969b40a906e59b0314fcc4f32dfce2193f964274
    path('profile/', profile_view, name='profile'),

]