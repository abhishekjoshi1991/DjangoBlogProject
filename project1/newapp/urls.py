from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('userlogin/',views.user_login,name='userlogin'),
    path('dashboard/',views.dashboard,name='dashboard'), 
    path('signup/',views.register,name='signup'),   
    path('logout_user/',views.logout_user,name='logout_user'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    path('addpost/',views.add_post,name='addpost'), 
    path('editpost/<int:id>',views.edit_post,name='editpost'),
    path('deletepost/<int:id>',views.delete_post,name='deletepost'),
    path('editprofile/',views.edit_profile,name='editprofile'),
]