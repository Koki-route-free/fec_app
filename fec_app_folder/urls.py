from django.urls import path
from . import views

app_name = 'fec_app_folder'
urlpatterns = [
    path('admins/login/', views.admins_login, name='admins/login/'),
    path('admins/login/solid/', views.admins_solid, name='admins/login/solid/'),
    path('admins/login/add_classroom/', views.admins_add_classroom, name='admins/login/add_classroom/'),
    path('admins/login/temporary/', views.admins_temporary, name='admins/login/temporary/'),
    path('users/top_page/', views.users_top_page, name='users/top_page/'),
    path('users/reviews/', views.users_reviews, name='users/reviews/'),
]