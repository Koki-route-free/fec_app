from django.urls import path
from . import views

app_name = 'fec_app_folder'
urlpatterns = [
    path('admins/login/', views.admins_login, name='admins_login'),
    path('admins/login/solid/', views.admins_solid, name='admins_login_solid'),
    path('admins/login/temporary/', views.admins_temporary, name='admins_login_temporary'),
    path('users/top_page/', views.users_top_page, name='users_top_page'),
    path('users/reviews/', views.users_reviews, name='users_reviews'),
]