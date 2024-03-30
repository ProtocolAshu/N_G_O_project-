from django.urls import path
from NMS_sw import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('application', views.application , name='application'),
    path('apply_fresh', views.apply_fresh , name='apply_fresh'),
    path('As_Student', views.As_Student, name='As_Student'),
    path('register_Donor', views.register_Donor, name='register_Donor'),
    path('donor_login', views.donor_login, name='donor_login'),
    path('eligibility', views.eligibility, name='eligibility'),
    path('renewal', views.renewal , name='renewal'),
    path('Donor', views.Donor , name='Donor'),
    path('donor_page', views.donor_page , name='donor_page'),
    
    path('reg_success', views.reg_success, name='reg_success'),
    path('home', views.home, name='home'),
    path('donorsview',views.donorsview,name='donorsview'),
    path('viewsingledonor',views.viewsingledonor,name='viewsingledonor'),
    path('login_admin',views.login_admin,name='login_admin'),
    
    path('Donor_availh',views.Donor_availh,name='Donor_availh'),
    path('studentlist',views.studentlist,name='studentlist'),
   
    path('estimates',views.estimates,name='estimates'),
    path('workingstats',views.workingstats,name='workingstats'),
    path('update_expenditure',views.update_expenditure,name='update_expenditure'),
    path('inventoryview',views.inventoryview,name='inventoryview'),
    path('showdonor/<donor_id>',views.viewsingledonor,name='show-donor'),
    path('clickunibook/<pledge_id>',views.clickub,name='click-ub'),
    path('clickpaid/<pledge_id>',views.clickp,name='click-paid'),
    path('updaterow/<row_id>',views.changeestimate,name='update-row'),
    path('updateinv/<inv_id>',views.inven,name='update-inv'),

    path('addexpend',views.updatetexp,name='aexpend'),
    path('viewpref',views.pref,name='viewpref'),
    path('est', views.est, name='est'),
    path('logout',views.logout,name='logout'),
    path('deletestudent/<student_id>',views.deletestudent,name='delete_student'),
    path('modifystudent/<student_id>',views.modifystudent,name='modify_student'),

]
# path('', views. , name=''),