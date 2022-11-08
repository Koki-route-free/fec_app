import datetime
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ClassCreateForm, AssetForm
from django.views.generic import CreateView, ListView, TemplateView
from django.db.models import Q
from .models import RoomDB, UserDB, SolidDB, TemporaryDB, AssetDB


class Admins_Solid_View(TemplateView):  
    template_name = 'admins/login/solid.html'
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        room_number = RoomDB.objects.order_by("room_number").values_list('room_number', flat=True)
        capacity = RoomDB.objects.order_by("room_number").values_list('capacity', flat=True)
        solid_room_number = SolidDB.objects.values_list('room_number', flat=True)
        solid_day_week = SolidDB.objects.values_list('day_week', flat=True)
        solid_time = SolidDB.objects.values_list('time', flat=True)
        solid_comment = SolidDB.objects.values_list('comment', flat=True)

        date = self.request.GET.get('date')
        if date:
            comment_1 = self.request.GET.getlist('comment_'+date+"1")
            comment_2 = self.request.GET.getlist('comment_'+date+"2")
            comment_3 = self.request.GET.getlist('comment_'+date+"3")
            comment_4 = self.request.GET.getlist('comment_'+date+"4")
            comment_5 = self.request.GET.getlist('comment_'+date+"5")
            comment_6 = self.request.GET.getlist('comment_'+date+"6")
            comment_num = [comment_1, comment_2, comment_3, comment_4, comment_5, comment_6]
            for i, comment in enumerate(comment_num):
                time = i + 1
                for c, r in zip(comment, room_number):
                    try:
                        obj = SolidDB.objects.get(day_week=int(date), time=time, room_number=r)
                    except SolidDB.DoesNotExist:
                        obj = None
                    if len(c)>0:
                        if obj:
                            obj.comment = c
                            obj.save()
                        else:
                            add = SolidDB(day_week=int(date), time=time, room_number=r, comment=c)
                            add.save()
                    else:
                        if obj:
                            obj.delete()
        for i in range(1,7):
            for j in range(1,7):
                comment_number = "comment_" + str(i) + str(j)
                class_comment_list = []
                for r in room_number:
                    if r in solid_room_number:
                        nums = [k for k, x in enumerate(solid_room_number) if x == r]
                        tf = []
                        for num in nums:
                            if solid_day_week[num]==i and solid_time[num]==j:
                                class_comment_list.append({comment_number:solid_comment[num]})
                                tf.append(1)
                            else:
                                tf.append(0)
                        if not 1 in tf:
                            class_comment_list.append({comment_number:""})
                    else:
                        class_comment_list.append({comment_number:""})
                if j==1:
                    comment_list = class_comment_list
                else:
                    for k, l in enumerate(class_comment_list):
                        comment_list[k].update(l)
            if i==1:
                comment_lists = comment_list
            else:
                for k, l in enumerate(comment_list):
                    comment_lists[k].update(l)
        for k, (l, m) in enumerate(zip(room_number, capacity)):
            a = {"room_number":l, "capacity":m}
            comment_lists[k].update(a)
        context["comment_lists"] = comment_lists
        context["result"] = "正常に登録されました"
        return context


class Admins_Temporary_View(TemplateView):
    template_name = "admins/login/temporary.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        room_id = self.request.GET.getlist('room_id')
        start_time = self.request.GET.getlist('start_time')
        finish_time = self.request.GET.getlist('finish_time')
        
        for i, j, k in zip(room_id, start_time, finish_time):
            if len(i)<1:
                break
            if not i[-4] in ["F", "H"]:
                context['result'] = "⚠︎入力がされていないカラムもしくは誤りがありました"
                return context
            if i[-3]=="2":
                room_number = "PCroom"
            else:
                room_number = i[-4:]
            try:
                str_date = j.split()[0]
                date = str_date.replace('/', '-')
                start = int(j.split()[1].replace(':',''))
                finish = int(k.split()[1].replace(':',''))
            except:
                context['result'] = "⚠︎入力がされていないカラムもしくは誤りがありました"
                return context
            if  start <= 1040:
                start_num = 1
            elif start <= 1230:
                start_num = 2
            elif start <= 1500:
                start_num = 3
            elif start <= 1650:
                start_num = 4
            elif start <= 1840:
                start_num = 5
            elif start <= 2030:
                start_num = 6
            else:
                start_num = -1

            if finish <= 1040:
                finish_num = 1
            elif finish <= 1230:
                finish_num = 2
            elif finish <= 1500:
                finish_num = 3
            elif finish <= 1650:
                finish_num = 4
            elif finish <= 1840:
                finish_num = 5
            else:
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
            else:
                continue
            for i in time:
                try:
                    obj = TemporaryDB.objects.get(room_number=room_number, time=i, date=date)
                except TemporaryDB.DoesNotExist:
                    obj = TemporaryDB(room_number=room_number, time=i, date=date)
                    obj.save()
        context['result'] = "正常に登録されました"
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


class Users_Top_page_View(TemplateView):
    template_name = 'users/top_page.html'
    def get_context_data(self, **kwargs):
        all_room = RoomDB.objects.order_by("room_number").values_list('room_number', flat=True)
        solid_room = SolidDB.objects
        temporary_room = TemporaryDB.objects
        
        research_date = self.request.GET.get('selectdate')
        time = self.request.GET.get('time')
        if research_date:
            date = datetime.datetime.strptime(research_date, '%Y-%m-%d')
        else:
            research_date = datetime.datetime.today()
            date = datetime.datetime.today()
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
        if time:
            date_commit = str(research_date).split('-')
            commit = date_commit[1] + "月" + date_commit[2] +"日" + str(time) +"限"
        else:
            commit = "現在"
            t_delta = datetime.timedelta(hours=9)
            JST = datetime.timezone(t_delta, 'JST')
            now = datetime.datetime.now(JST)
            d = int(f'{now:%H%M}')
            if d < 1040:
                time = 1
            elif d < 1230:
                time = 2
            elif d < 1500:
                time = 3
            elif d < 1650:
                time = 4
            elif d < 1840:
                time = 5
            else:
                time = 6
            
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
        # 配列として認識するため（テスト時のエラー回避）
        if len(all_room)>2:
          for i in all_room:
            if "F6" in i:
                room6.append(i)
                if i in use_room:
                    room6_tf.append("  ×")
                elif day_num in [6,7]:
                    room6_tf.append("  ×")
                else:
                    room6_tf.append(" ◯")
            elif "F5" in i:
                room5.append(i)
                if i in use_room:
                    room5_tf.append("  ×")
                elif day_num in [6,7]:
                    room5_tf.append("  ×")
                else:
                    room5_tf.append(" ◯")
            elif "F4" in i:
                room4.append(i)
                if i in use_room:
                    room4_tf.append("  ×")
                elif day_num in [6,7]:
                    room4_tf.append("  ×")
                else:
                    room4_tf.append(" ◯")
            elif ("F3" in i) or ("H" in i):
                room3.append(i)
                if i in use_room:
                    room3_tf.append("  ×")
                elif day_num in [6,7]:
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
        result["commit"] = commit
        return result

admins_solid = Admins_Solid_View.as_view()
admins_add_classroom = Admins_Add_classroom_View.as_view()
admins_temporary = Admins_Temporary_View.as_view()
admins_login = Admins_Login_View.as_view()
users_reviews = Users_Reviews_View.as_view()
users_top_page = Users_Top_page_View.as_view()