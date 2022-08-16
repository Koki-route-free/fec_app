from django.shortcuts import render
from django.views import View

class Admins_Solid_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'admins/solid.html')


class Admins_Temporary_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'admins/temporary.html')


class Admins_Login_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'admins/login.html')


class Users_Reviews_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'users/reviews.html')

    
class Users_Top_page_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'users/top_page.html')


admins_solid = Admins_Solid_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()