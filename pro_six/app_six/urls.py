from django.urls import path
from app_six import views


app_name = 'app_six'

urlpatterns = [
   path('base/', views.base, name= "base"),
   path('registration/', views.register, name="registration"),
   path('user_login/', views.user_login, name="user_login")

]
