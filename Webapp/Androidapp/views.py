# views.py

from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render,redirect
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import AndroidApp, UserProfile, UserTask
from .serializers import AndroidAppSerializer, UserProfileSerializer, UserTaskSerializer
from .forms import CustomAndroidAppForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,AdminRegistrationForm,AdminLoginForm
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Androidapp.models import Admin
from django.http import HttpResponse

class AndroidAppListCreateView(generics.ListCreateAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
def home(request):
    return render(request,'base.html')

def admin_registration(request):
    # Check if an admin user already exists
    if Admin.objects.exists():
        # Redirect to the appropriate page, indicating that admin already exists
        return HttpResponse("Admin user already exists.")

    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            admin_name = form.cleaned_data['admin_name']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Perform password validation here if needed

            # Create and save the Admin instance
            admin = Admin.objects.create(admin_name=admin_name, password=password, confirm_password=confirm_password)

            # Redirect to the desired page after successful registration
            return add_app(request)  # Change 'login' to the appropriate URL name
    else:
        form = AdminRegistrationForm()
    return render(request, 'createadmin.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            admin_name = form.cleaned_data['admin_name']
            password = form.cleaned_data['password']

            # Authenticate admin
            admin = authenticate(username=admin_name, password=password)
            if admin is not None:
                login(request, admin)
                return add_app(request)  # Change to appropriate URL
            else:
                return HttpResponse("Invalid admin credentials.")

    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})

def add_app(request):
    success_message = None

    if request.method == 'POST':
        form = CustomAndroidAppForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            if 'image' in request.FILES:
                app.image = request.FILES['image']
            app.save()
            success_message = "App created successfully!"
    else:
        form = CustomAndroidAppForm()

    return render(request, 'app_adding.html', {'form': form, 'success_message': success_message})

def display_android_app(request, app_id):
    android_app = AndroidApp.objects.get(pk=app_id)  # Fetch the Android app data from the API
    return render(request, 'admin_view.html', {'android_app': android_app})



# class UserProfileView(generics.RetrieveAPIView):
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user.profile



def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return user_login(request)  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return user_view(request)  # Redirect to dashboard or desired page
    else:
        form = UserLoginForm()

    return render(request, 'Userlogin.html', {'form': form})
def user_view(request):
    app = AndroidApp.objects.all()
    return render(request,'user_view.html',{'app':app})
def app_view(request,p):
    b=AndroidApp.objects.get(id=p)
    return render(request,'app_view.html',{'i':b})



class UserTaskSubmitView(generics.CreateAPIView):
    serializer_class = UserTaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




