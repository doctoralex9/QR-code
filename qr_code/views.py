from django.shortcuts import render
from qrcode import make
from django.conf import settings
from time import time
from django.contrib.auth.decorators import login_required  # Add login_required decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse  # Import reverse function

# Create your views here.


def generate_QR_code(request):
    if request.method == 'POST':
        data = request.POST['text']
        img = make(data)
        img_name = f'{str(time())}.png'
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        context = {
            'img_name': img_name
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

# Adjust the login_user view function to return JsonResponse with appropriate status codes and data
@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Return a JsonResponse with success: true and the redirect URL
            return JsonResponse({'success': True, 'redirect_url': reverse('profile')})
    return HttpResponseBadRequest()  # Return bad request if login fails

@login_required
@api_view(['GET'])
def profile_view(request):
    # Retrieve the current user
    user = request.user
    # Render the profile.html template with the user object in the context
    return render(request, 'profile.html', {'user': user})

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)