from django.urls import path, re_path
from . import views


app_name = 'Accounts'

urlpatterns = [
    path('SignUp/',views.signUp,name='SignUp'),
    path('loginUser/',views.login_meth,name='Loginview'),
    path('Completeinfo/',views.editinfo,name='editinfo'),
    path('Logout/',views.logOut,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.editUser,name='userEdit'),
    path('profile/password/',views.changemdp,name="passwordchange")
]