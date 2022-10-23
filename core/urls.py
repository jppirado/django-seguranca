
from django.urls import path , include 
from django.contrib.auth  import views as auth_views
from .views import MyProfileView , LoginView

urlpatterns = [
    path('login/' , LoginView.as_view() , name='login'), 
    path('logout/' , auth_views.LogoutView.as_view() , name='logout' ),
    path('social-auth' , include ('social_django.urls' , namespace='social')),
    path('meuperfil' ,  MyProfileView.as_view() , name='meuperfil' ), 
]