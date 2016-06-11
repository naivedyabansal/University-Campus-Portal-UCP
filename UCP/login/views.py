"""
Views file for Login App

contains views for the frontend pages of the Login App
"""

from django.shortcuts import render, redirect
from django.views.generic import View

from login.functions import login, register, forgot_password, reset_password, get_response_text
from UCP.constants import result

class Login(View):
    
    def get(self, request):
        context = {}
        context["is_login_page"] = True
        
        if not 'email' in request.GET:
            return render(request, 'login-register.html', context)
        
        response = login(request)
        
        if response["result"] == result.RESULT_SUCCESS:
            return redirect('/discussions/')
        else:
            context["message"] = get_response_text(response)
        
            return render(request, 'login-register.html', context)


class Register(View):
    
    def get(self, request):
        return render(request, 'login-register.html')
        
    def post(self, request):

        context={}
        
        response = register(request)
        
        context["message"] = get_response_text(response)
        
        return render(request, 'login-register.html', context)
        

class ForgotPassword(View):
    
    def get(self, request):
        
        context={}
        response = forgot_password(request)
        context["message"] = get_response_text(response)
        
        if(response["result"] == 0):
            context["is_login_page"] = True
            print context
            return render(request, 'login-register.html', context)
        if(response["result"] == 1):
            return render(request, 'reset-password.html', context)
       
        
class ResetPassword(View):
    
    def post(self, request):
        
        context={}
        response = reset_password(request)
        context["message"] = get_response_text(response)
        
        if(response["result"] == 1):
            context["is_login_page"] = True
            return render(request, 'login-register.html', context)
        if(response["result"] == 0):
            return render(request, 'reset-password.html', context)
        
        
        
        
