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
    path('reg_success', views.reg_success, name='reg_success'),
    path('home', views.home, name='home'),
    # path('Donor', views.Donor , name='Donor'),
    path('viewDonor',views.donorview,name='viewDonor'),
    path('admin_login',views.admin_login,name='login_admin'),
    path('logout',views.logout,name='logout'),
    path('pledgehist',views.Donor_availh,name='pledgehist'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('deletestudent/<student_id>',views.deletestudent,name='delete_student'),
    path('modifystudent/<student_id>',views.modifystudent,name='modify_student'),
    path('editesttbl',views.editest,name='editesttbl'),
    path('viewworking',views.vstats,name='viewworking'),
    path('viewpref',views.pref,name='viewpref'),
    path('maintaininv',views.minventory,name='maintaininv'),
    path('showdonor/<donor_id>',views.viewdonor,name='show-donor'),
    path('clickunibook/<pledge_id>',views.clickub,name='click-ub'),
    path('clickpaid/<pledge_id>',views.clickp,name='click-paid'),
    path('updaterow/<row_id>',views.changeestimate,name='update-row'),
    path('updateinv/<inv_id>',views.inven,name='update-inv'),
    path('viewexpenditure',views.exph,name='vexp'),
    path('addexpend',views.updatetexp,name='aexpend'),
    

]
# path('', views. , name=''),