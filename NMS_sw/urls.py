from django.urls import path
from NMS_sw import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('As_Student', views.As_Student, name='As_Student'),
    path('register_Donor', views.register_Donor, name='register_Donor'),
    path('login', views.login, name='login'),
    path('eligibility', views.eligibility, name='eligibility'),
    path('renewal', views.renewal , name='renewal'),
    path('application', views.application , name='application'),
    path('apply_fresh', views.apply_fresh , name='apply_fresh'),
    path('home', views.home, name='home'),
]
# path('', views. , name=''),