from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from .forms import LoginForm, ClassCreateForm
from django.views.generic import CreateView, ListView
from django.db.models import Q
from django.contrib.auth import login, authenticate
from .models import RoomDB, UserDB, SolidDB, TemporaryDB, AssetDB


class Admins_Solid_View(ListView):  
    template_name = 'admins/login/solid.html'
    model = RoomDB
    ordering = 'room_number'


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
        context = {'F3classrooms': ["F301", "F302", "F303", "F304", "F305", "F306", "F307", "F308", "F309", "F310", "F311", "F312"],
                   'F4classrooms': ["F401", "F402", "F403", "F404", "F405", "F406", "F407", "F408", "F409", "F410", "F411"],
                   'F5classrooms': ["F501", "F502", "F503", "F504", "F505", "F506", "F507", "F508", "F509", "F510", "F511", "F512", "F513"],
                   'F6classrooms': ["F601", "F602", "F603", "F604", "F605", "F606", "F607", "F608"],}
        return render(request, 'users/top_page.html', context)


admins_solid = Admins_Solid_View.as_view()
admins_add_classroom = Admins_Add_classroom_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()