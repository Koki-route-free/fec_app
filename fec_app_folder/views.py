from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from .forms import LoginForm, ClassCreateForm
from django.views.generic import CreateView, ListView
from django.db.models import Q
from django.contrib.auth import login, authenticate
from .models import UserDB, SolidDB, TemporaryDB, AssetDB


class Admins_Solid_View(CreateView):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'admins/login/solid.html')


class Admins_Temporary_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'admins/login/temporary.html')
    
    
class Admins_Add_classroom_View(CreateView):
    form_class = ClassCreateForm
    template_name = 'admins/login/add_classroom.html'
    success_url = reverse_lazy('fec_app_folder:admins/login/solid/')


class Admins_Login_View(LoginView):  
    form_class = LoginForm
    template_name = 'admins/login.html'


class Users_Reviews_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'users/reviews.html')

    
class Users_Top_page_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'users/top_page.html')


admins_solid = Admins_Solid_View.as_view()
admins_add_classroom = Admins_Add_classroom_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()