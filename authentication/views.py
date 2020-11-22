from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.urls import reverse
from django.contrib import auth
# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request,'authentication/register.html')

    def post(self,request):
        
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        context={
            'fieldValues':request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request, 'Password too short!')
                    return render(request,'authentication/register.html')
                
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.save()
                messages.success(request,'Account successfully created')
                return render(request,'authentication/register.html')

        return render(request,'authentication/register.html')

class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body) #creates a dictionary
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should only contain alpha-numberic characters'},status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry, username already taken, choose a different one.'},status=400)
        return JsonResponse({'username_valid':True})

class EmailValidationView(View):
    def post(self, request):
        data=json.loads(request.body) #creates a dictionary
        email=data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'Invalid Email'},status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'Sorry, Email is already in use, please sign in.'},status=400)
        return JsonResponse({'email_valid':True})


class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        if username and password:
            user=auth.authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request,'Welcome, '+user.username+'. You are now logged in')

                    return redirect('activity')
            else:
                messages.error(request,"Invalid username/password.")
                return render(request,'authentication/login.html')
        else:
            messages.error(request,'Please fill all the fields.')
            return render(request,'authentication/login.html')

class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,'Logged out successfully.')
        return redirect('login')