from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ClassCreateForm, AssetForm
from django.views.generic import CreateView, ListView, TemplateView
from django.db.models import Q
from django.contrib.auth import login, authenticate
from .models import RoomDB, UserDB, SolidDB, TemporaryDB, AssetDB


class Admins_Solid_View(ListView):  
    model = RoomDB
    template_name = 'admins/login/solid.html'
    ordering = 'room_number'
    def get_context_data(self, **kwargs):
        room_number = RoomDB.objects.values_list('room_number', flat=True)
        capacity = RoomDB.objects.values_list('capacity', flat=True)
        
        date = self.request.GET.get('date')
        class_1 = self.request.GET.getlist('class_1')
        class_2 = self.request.GET.getlist('class_2')
        class_3 = self.request.GET.getlist('class_3')
        class_4 = self.request.GET.getlist('class_4')
        class_5 = self.request.GET.getlist('class_5')
        class_6 = self.request.GET.getlist('class_6')
        class_num = [class_1, class_2, class_3, class_4, class_5, class_6]
        comment_1 = self.request.GET.getlist('comment_1')
        comment_2 = self.request.GET.getlist('comment_2')
        comment_3 = self.request.GET.getlist('comment_3')
        comment_4 = self.request.GET.getlist('comment_4')
        comment_5 = self.request.GET.getlist('comment_5')
        comment_6 = self.request.GET.getlist('comment_6')
        comment_num = [comment_1, comment_2, comment_3, comment_4, comment_5, comment_6]
        for i, (class_tf, comment) in enumerate(zip(class_num, comment_num)):
            time = i +1
            for a, c, r in zip(class_tf, comment, room_number):
                if len(a)>0:
                    try:
                        obj = SolidDB.objects.get(room_number=r, time=time, day_week=date)
                    except SolidDB.DoesNotExist:
                        obj = SolidDB(room_number=r, time=time, day_week=date, comment=c)
                        obj.save()
        context = super().get_context_data(**kwargs)
        context["room_number"] = room_number
        context["capacity"] = capacity
        context["result"] ="正常に登録されました"
        return context


class Admins_Temporary_View(TemplateView):
    template_name = "admins/login/temporary.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        room_id = self.request.GET.getlist('room_id')
        start_time = self.request.GET.getlist('start_time')
        finish_time = self.request.GET.getlist('finish_time')
        
        if len(room_id)==len(start_time) and len(room_id)==len(finish_time) and len(room_id)>0:
            for i, j, k in zip(room_id, start_time, finish_time):
                if len(i)<1:
                    break;
                if (i[-4]=="F") or (i[-4]=="H"):
                    room_number = i[-4:]
                else:
                    room_number = i[-6:]
                str_date = j.split()[0]
                date = str_date.replace('/', '-')
                start = j.split()[1]
                finish = k.split()[1]
                if start=="9:00":
                    start_num = 1
                elif start=="10:50":
                    start_num = 2
                elif start=="13:20":
                    start_num = 3
                elif start=="15:10":
                    start_num = 4
                elif start=="17:00":
                    start_num = 5
                elif start=="18:50":
                    start_num = 6

                if finish=="10:40":
                        finish_num = 1
                elif finish=="12:30":
                    finish_num = 2
                elif finish=="15:00":
                    finish_num = 3
                elif finish=="16:50":
                    finish_num = 4
                elif finish=="18:40":
                    finish_num = 5
                elif finish=="20:30":
                    finish_num = 6
                sum = finish_num - start_num
                if sum==0:
                    time = [start_num]
                elif sum==1:
                    time = [start_num, finish_num]
                elif sum==2:
                    time = [start_num, start_num+1, finish_num]
                elif sum==3:
                    time = [start_num, start_num+1, start_num+2, finish_num]
                elif sum==4:
                    time = [start_num, start_num+1, start_num+2, start_num+3, finish_num]
                elif sum==5:
                    time = [start_num, start_num+1, start_num+2, start_num+3, start_num+4, finish_num]
                for i in time:
                    try:
                        obj = TemporaryDB.objects.get(room_number=room_number, time=i)
                    except TemporaryDB.DoesNotExist:
                        obj = TemporaryDB(room_number=room_number, time=i, date=date)
                        obj.save()
            context['result'] = "正常に登録されました"
        else:
            context['result'] = "入力がされていないカラムがあります"
        return context



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


class Users_Top_page_View(ListView):
    template_name = 'users/top_page.html'
    model = RoomDB
    
    def get_context_data(self, **kwargs):
        all_room = RoomDB.objects.values_list('room_number', flat=True)
        solid_room = SolidDB.objects
        temporary_room = TemporaryDB.objects
        
        date = self.request.GET.get('date')
        time = self.request.GET.get('time')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d')
        else:
            date = datetime.today()
        day = date.strftime('%A')
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
        
        if len(all_room)>2:
            for i in all_room:
                if "F6" in i:
                    room6.append(i)
                    if i in use_room:
                        room6_tf.append("  ×")
                    else:
                        room6_tf.append(" ◯")
                elif "F5" in i:
                    room5.append(i)
                    if i in use_room:
                        room5_tf.append("  ×")
                    else:
                        room5_tf.append(" ◯")
                elif "F4" in i:
                    room4.append(i)
                    if i in use_room:
                        room4_tf.append("  ×")
                    else:
                        room4_tf.append(" ◯")
                elif ("F3" in i) or ("H" in i):
                    room3.append(i)
                    if i in use_room:
                        room3_tf.append("  ×")
                    else:
                        room3_tf.append(" ◯")
                else:
                    room2.append(i)
                    if i in use_room:
                        room2_tf.append("  ×")
                    else:
                        room2_tf.append(" ◯")
        result = super().get_context_data()
        result["room2"] = room2
        result["room2_tf"] = room2_tf
        result["room3"] = room3
        result["room3_tf"] = room3_tf
        result["room4"] = room4
        result["room4_tf"] = room4_tf
        result["room5"] = room5
        result["room5_tf"] = room5_tf
        result["room6"] = room6
        result["room6_tf"] = room6_tf
            
        return result

admins_solid = Admins_Solid_View.as_view()
admins_add_classroom = Admins_Add_classroom_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()