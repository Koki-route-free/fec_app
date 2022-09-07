from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ClassCreateForm, AssetForm
from django.views.generic import CreateView, ListView
from django.db.models import Q
from django.contrib.auth import login, authenticate
from .models import RoomDB, UserDB, SolidDB, TemporaryDB, AssetDB


class Admins_Solid_View(ListView):  
    model = RoomDB
    template_name = 'admins/login/solid.html'
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
    model = AssetDB
    form_class = AssetForm
    template_name = 'users/reviews.html'
    success_url = reverse_lazy('fec_app_folder:users/top_page/')

    
# class Users_Top_page_View(View):  
#     def get(self, request, *args, **kwargs):  
#         return render(request, 'users/top_page.html')


class Users_Top_page_View(ListView):
    template_name = 'users/top_page.html'
    model = RoomDB
    
    def get_context_data(self, **kwargs):
        all_room = RoomDB.objects.values_list('room_number', flat=True)
        # all_room = []
        # if len(room)>1:
        #     for i in room:
        #         all_room.append(i.room_number)
        solid_room = SolidDB.objects
        temporary_room = TemporaryDB.objects
        
        date = self.request.GET.get('date')
        time = self.request.GET.get('time')
        # day = date.strftime('%A')
        day = "Sunday"
        if day == "Sunday":
            day_num = 7
        elif day == "Monday":
            day_num = 1
        elif day == "Tuesday":
            day_num = 2
        elif day == "Wednesday":
            day_num = 3
        elif day == "Thursday":
            day_num = 4
        elif day == "Friday":
            day_num = 5
        elif day == "Saturday":
            day_num = 6
        
        solid_result = solid_room.filter(Q(day_week__exact=day_num)&Q(time__exact=time))
        temporary_result = temporary_room.filter(Q(date__exact=date)&Q(time__exact=time))
        
        solid_use_room = solid_result.values_list('room_number', flat=True)
        temporary_use_room = temporary_result.values_list('room_number', flat=True)
        use_room = solid_use_room.union(temporary_use_room)
        # 重複をなくす
        
        room2 = []
        room2_tf = []
        room3 = []
        room3_tf = []
        room4 = []
        room4_tf = []
        room5 = []
        room5_tf = []
        room6 = []
        room6_tf = []
        
        result = super().get_context_data()
        
        if len(all_room)>2:
            for i in all_room:
                if "F6" in i:
                    room6.append(i)
                    if i in use_room:
                        room6_tf.append(" ×")
                    else:
                        room6_tf.append(" ◯")
                elif "F5" in i:
                    room5.append(i)
                    if i in use_room:
                        room5_tf.append(" ×")
                    else:
                        room5_tf.append(" ◯")
                elif "F4" in i:
                    room4.append(i)
                    if i in use_room:
                        room4_tf.append(" ×")
                    else:
                        room4_tf.append(" ◯")
                elif "F3" in i:
                    room3.append(i)
                    if i in use_room:
                        room3_tf.append(" ×")
                    else:
                        room3_tf.append(" ◯")
                else:
                    room2.append(i)
                    if i in use_room:
                        room2_tf.append(" ×")
                    else:
                        room2_tf.append(" ◯")
            room2 = ["pcroom"]
            room2_tf = ["◯"]
            # result =  {
            #     "room2":room2, "room2_tf":room2_tf, 
            #     "room3":room3, "room3_tf":room3_tf, 
            #     "room4":room4, "room4_tf":room4_tf, 
            #     "room5":room5, "room5_tf":room5_tf, 
            #     "room6":room6, "room6_tf":room6_tf, 
            # }
            result["room2"] = [room2, room2_tf]
            result["room3"] = room3
            result["room3_tf"] = room3_tf
            result["room4"] = room4
            result["room4_tf"] = room4_tf
            result["room5"] = room5
            result["room5_tf"] = room5_tf
            result["room6"] = room6
            result["room6_tf"] = room6_tf
        else:
            result["none"] = "none"
        return result

# class Users_Top_page_View(View):  
#     def get(self, request, *args, **kwargs):  
#         return render(request, 'users/top_page.html')
#         context = {'F3classrooms': ["F301", "F302", "F303", "F304", "F305", "F306", "F307", "F308", "F309", "F310", "F311", "F312"],
#                    'F4classrooms': ["F401", "F402", "F403", "F404", "F405", "F406", "F407", "F408", "F409", "F410", "F411"],
#                    'F5classrooms': ["F501", "F502", "F503", "F504", "F505", "F506", "F507", "F508", "F509", "F510", "F511", "F512", "F513"],
#                    'F6classrooms': ["F601", "F602", "F603", "F604", "F605", "F606", "F607", "F608"],}
#         return render(request, 'users/top_page.html', context)

admins_solid = Admins_Solid_View.as_view()
admins_add_classroom = Admins_Add_classroom_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()