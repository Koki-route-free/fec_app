from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from .forms import LoginForm, ClassCreateForm, AssetForm
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
    model = RoomDB
    form_class = ClassCreateForm
    template_name = 'admins/login/add_classroom.html'
    success_url = reverse_lazy('fec_app_folder:admins/login/solid/')


class Admins_Login_View(LoginView):  
    form_class = LoginForm
    template_name = 'admins/login.html'


class Users_Reviews_View(CreateView):  
    def post(self, request, *args, **kwargs):
        form = AssetForm(data=request.POST)
        if form.is_valid():
            form.save()
            student_number = form.cleaned_data.get('student_number')
            room_number = form.cleaned_data.get('room_number')
            use_num = form.cleaned_data.get('use_num')
            classification = form.cleaned_data.get('classification')
            
            contents = authenticate(name=name, address=address, homepage=homepage, classification=classification, telephone=telephone)
            login(request, contents)
            return redirect('/')
        return render(request, 'fill_in_time_app/create_contents.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = ContentsCreateForm(request.POST)
        return  render(request, 'fill_in_time_app/create_contents.html', {'form': form,})

    
class Users_Top_page_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'users/top_page.html')


admins_solid = Admins_Solid_View.as_view()
admins_add_classroom = Admins_Add_classroom_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()