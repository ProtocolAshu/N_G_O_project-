from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .form import Studentform,Donor_availform
from datetime import datetime
from .models import Student,renewal, register_Donor, Donor_avail, totalmoney,estimations,inventory,expenditure,exphist,Admin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def admin_login(request):
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        us=Admin.objects.first()
        if username==us.username:
            if password==us.password:
                user=authenticate(username=username,password=password)
                if user is not None:
                    user.is_staff=True
                    login(request,user)
                    messages.success(request,"successfully logged in")
                    return render(request,'adminpage.html',{})                
            else:
                messages.success(request,"Please enter correct password")
                return redirect('/adminlogin')
        else:
            messages.success(request,"Please enter correct username")
            return redirect('/adminlogin')
    else:
        if (request.user.is_authenticated and request.user.is_staff):
            return render(request,'adminpage.html',{})
        return render(request,'login_admin.html',{})
    
def reg_success(request):
    # Your logic here if needed
    return render(request, 'reg_success.html')

def As_Student(request):
    # if ((request.user.is_authenticated) and (request.user.is_staff)):
    #     if request.method == 'POST':
    #         new_student = Student()
    #         new_student.fullname=request.POST['fullname']
    #         new_student.Grade=request.POST['Grade']
    #         new_student.income=int(request.POST['income'])
    #         new_student.money_needed=request.POST['money_needed']
    #         if "books" in request.POST:
    #             new_student.books=request.POST['books']
    #         if "uniform" in request.POST:
    #             new_student.uniform=request.POST['uniform']
    #         new_student.performance=float(request.POST['performance'])
    #         new_student.gender=request.POST['gender']
    #         new_student.__score__()
    #         new_student.save()
    #         messages.info(request,"Student added!")
    #         return render(request,'admin_page.html')    
        return render(request,'As_Student.html')

def aple(request):
    if (request.user.is_authenticated):
        submitted=False
        if request.method == "POST":
            form=Donor_availform(request.POST)
            if form.is_valid():
                dnr=register_Donor.objects.filter(user=request.user).first()
                Donor_availobj=Donor_avail(money=request.POST['money'],books=request.POST['books'],uniform=request.POST['uniform'],frequency=request.POST['frequency'],register_donor=dnr,status=False,ubstatus=False)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # Donor_availobj.money=form['money']
                # Donor_availobj.books=form['books']
                # Donor_availobj.uniform=form['uniform']
                # Donor_availobj.register_donor=request.user
                # Donor_availobj.status=False
                Donor_availobj.time=datetime.now()
                Donor_availobj.lastpaid=datetime.now()
                Donor_availobj.save()
                messages.info(request,"Donor_availd!")
                return HttpResponseRedirect('/aple?submittted=True')
        else:
            form=Donor_availform
            if 'submitted' in request.GET:
                submitted=True
        return render(request,'addDonor_avail.html',{'form':form})

def donor_login(request):
    register_donor=register_Donor()
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        # print("010")
        register_donor.user=authenticate(username=username,password=password)
        # print("100")
        if register_donor.user is not None:
            # print("777")
            login(request,register_donor.user)
            messages.success(request,"Welcome, you are successfully logged in!!")
            return render(request,'donorpage.html',{})
        else:
            # print("011")
            messages.success(request,"Please enter correct username or password ")
            return redirect('/donorlogin')
    else:
        if (request.user.is_authenticated):
            return render(request,'donorpage.html',{})
        return render(request,'login_donor.html',{})

# def register_Donor(request):
#     register_donor=register_Donor()
#     if request.method == "POST":
#         # Extract form data
#         name = request.POST("Name")
#         email = request.POST("Email")
#         Number = request.POST("Number")
#         username = request.POST('username')
#         password = request.POST("Password")
#         C_password = request.POST("Confirm_Password")

#     try:
#         if password == C_password:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Already Taken')
#                 return redirect('register_Donor.html')
#             else:
#                 register_donor = register_Donor()
#                 register_donor.user = User.objects.create_user(name=name, email=email, username=username, password=password)
#                 register_donor.phone = Number
#                 register_donor.save()

#                 messages.info(request, 'register_Donor account created')
#                 return redirect('/')
#         else:
#             messages.info(request, 'Password does not match')
#             return redirect('register_Donor.html')
#     except Exception as e:
#             messages.error(request, f"Error occurred: {e}")
#             return redirect('register_Donor.html')
def register_Donor(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        Number = request.POST.get("Number")
        username = request.POST.get('username')
        password = request.POST.get("Password")
        C_password = request.POST.get("Confirm_Password")

        try:
            if password == C_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Taken')
                    return redirect('register_Donor.html')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    register_donor = register_Donor.objects.create(user=user, phone=Number)
                    messages.info(request, 'Donor account created successfully')
                    return redirect('/')
            else:
                messages.info(request, 'Passwords do not match')
                return redirect('register_Donor.html')
        except Exception as e:
            messages.error(request, f"Error occurred: {e}")
            return redirect('register_Donor.html')
    else:
        return render(request, 'register_Donor.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    return render(request, 'login.html')

def donorview(request):
    donors_list=register_Donor.objects.all()
    return render(request,'donorsview.html',{'donor_list':donors_list})

def viewdonor(request, donor_id):
    register_donor = register_Donor.objects.get(id=donor_id)
    return render(request,'donorview.html',{'register_donor':register_donor})

def clickub(request, pledge_id):
     if ((request.user.is_authenticated) and (request.user.is_staff)):
        D0nor_Avail = Donor_avail.objects.get(pk=pledge_id)
        if D0nor_Avail.ubstatus==False:
            D0nor_Avail.ubstatus=True
        D0nor_Avail.save()
        return redirect('/pledgehist')

def Donor_availh(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        Semiannually=Donor_avail.objects.filter(frequency="Semiannually")
        Annually=Donor_avail.objects.filter(frequency="Annually")
        for sDonor_avail in Semiannually:
            tyet=(datetime.now().month - sDonor_avail.time.month) + 12*(datetime.now().year-sDonor_avail.time.year)
            tpyet=(sDonor_avail.lastpaid.month - sDonor_avail.time.month) + 12*(sDonor_avail.lastpaid.year-sDonor_avail.time.year)
            months=int(tyet)
            month=int(tpyet)
            mon=(months%12)
            monp=(month%12)
            if (mon>6 & monp<=6) | (mon<=6 & monp>6):
                sDonor_avail.status=False
                sDonor_avail.save()
        for sDonor_avail in Annually:
            tyet=(datetime.now().month - sDonor_avail.time.month) + 12*(datetime.now().year-sDonor_avail.time.year)
            tpyet=(sDonor_avail.lastpaid.month - sDonor_avail.time.month) + 12*(sDonor_avail.lastpaid.year-sDonor_avail.time.year)
            months=int(tyet)
            month=int(tpyet)
            mon=(months%24)
            monp=(month%24)
            if (mon>12 & monp<=12) | (mon<=12 & monp>12):
                sDonor_avail.status=False
                sDonor_avail.save()
            
        Donor_avail_list=Donor_avail.objects.all()
        
        return render(request,'Donor_availhistory.html',{'Donor_availlist':Donor_avail_list})


def eligibility(request):
    return render(request, 'eligibility.html')

def renewal(request):
    # if request.method == "POST":
    #     File_upload = request.FILES.get("fileUpload")
        
    #     try:
    #         R_user = Renewal.objects.create(fileUpload=File_upload)
    #         R_user.save()
    #         return HttpResponse("Uploaded Successfully")
    #     except Exception as e:
    #         return HttpResponse(f"Error occurred: {e}")

    #         # Proceed with renewal process
    #         # Add your renewal logic here

    return render(request, 'renewal.html')

def application(request):
    return render(request, 'application.html')

def apply_fresh(request):
    if request.method=="POST":
        F_name=request.POST.get("fullName")
        Gender=request.POST.get("gender")
        Age=request.POST.get("age")
        Grade=request.POST.get("Grade")
        S_name=request.POST.get("schoolName")
        Performance=request.FILES.get("performance")
        G_name=request.POST.get("guardianName")
        F_income=request.POST.get("income")
        Password=request.POST.get("password")
        C_password=request.POST.get("confirmPassword")
        # print(F_name, Gender, Age, Class, S_name, Performance, G_name, F_income, Password, C_password)

        if Password != C_password:
            return render(request, 'apply_fresh.html', {'error_message': 'Both Passwords Do Not Match'})
        try:
            S_user = Student.objects.create(fullName=F_name, password=Password, gender=Gender, age=Age, Grade=Grade, schoolName=S_name, performance=Performance, guardianName=G_name, income=F_income)
            S_user.save()
            return HttpResponse("Registration Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")

    return render(request, 'apply_fresh.html')

def clickp(request, pledge_id):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        Donor_Avail = Donor_avail.objects.get(pk=pledge_id)
        if Donor_Avail.status==False:
            Donor_Avail.status=True
            Donor_Avail.lastpaid=datetime.now()
            money=int(totalmoney.objects.all().count())
            if money>0:
                # print(money)
                # print("111")
                funds=totalmoney.objects.first()
                funds.Sum=int(Donor_Avail.money)+int(funds.Sum)
                funds.save()
            else:
                # print("222")
                funds=totalmoney(Sum=int(Donor_Avail.money))
                funds.save()
        else:
            Donor_Avail.status=False
        Donor_Avail.save()
        return redirect('/pledgehist')
    
    
    
def delstu(request):
    pass
def editest(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        est_list=estimations.objects.all()

        return render(request,'estimates.html',{'estimationlist':est_list})
def changeestimate(request,row_id):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        row=estimations.objects.get(pk=row_id)
        if request.method == 'POST':
                row.books=request.POST['book']
                row.uniforms=request.POST['uniform']
                row.save()
        return render(request,'est.html',{'row':row})

def vstats(request):
    # inv=inventory.objects.all()
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        stu=Student.objects.all()
        money=int(0)
        books=[0,0,0,0,0,0,0,0]
        uniforms=[0,0,0,0,0,0,0,0]
        for stud in stu:
            money=money+int(stud.money_needed)
            if stud.books:
                books[stud.Grade]=books[stud.Grade]+1
            if stud.uniform:
                uniforms[stud.Grade]=uniforms[stud.Grade]+1
        for s in range(1,6,1):
            inv=inventory.objects.filter(Grade=s).first()
            if books[s]>0:
                if books[s]>inv.books:
                    books[s]=books[s]-int(inv.books)
                else:
                    books[s]=0
            if uniforms[s]>0:
                if uniforms[s]>inv.uniforms:
                    uniforms[s]=uniforms[s]-int(inv.uniforms)
                else:
                    uniforms[s]=0
            es=estimations.objects.filter(Grade=s).first()
            money=money+books[s]*int(es.books)+uniforms[s]*int(es.uniforms)
        funds=totalmoney.objects.first()
        if funds.Sum >= money:
            messages.info(request,"Congrats!! we have enough funds")
        else:
            messages.info(request,"Caution not enough funds!! short by"+ str(money-funds.Sum)+" Rupees" )
        return render(request,'workingstats.html',{'money':money,'totalmoney':funds})

def pref(request):
    pass

def minventory(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        inv=inventory.objects.all()
        
        return render(request,'inventoryview.html',{'inventorylist':inv})
def inven(request,inv_id):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        inv=inventory.objects.get(pk=inv_id)
        if request.method=='POST':
            inv.books=request.POST['book']
            inv.uniforms=request.POST['uniform']
            inv.save()
        return render(request,'inve.html',{'inven':inv})
def updatetexp(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        money=expenditure.objects.all().count()
        if request.method=='POST':
            m=int(request.POST['money'])
            r=request.POST['reason']
            tam=totalmoney.objects.first()
            if tam.Sum> m:
                tam.Sum=tam.Sum-int(m)
                tam.save()
            else:
                # print("333")
                messages.info(request,'not enough money with NGO')
                return redirect('/addexpend')
            if money>0:
                # print("222")
                texp=expenditure.objects.first()
                texp.exp=texp.exp+int(m)
                texp.save()
            else:
                # print("111")
                texp=expenditure(exp=int(m))
                texp.save()
            t=exphist(expe=int(m),rec=r)
            t.save()
            return redirect('/viewexpenditure')
        return render(request,'update_expenditure.html')

def exph(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        m=expenditure.objects.all().count()
        if m>0:
            # print(m)
            expend=exphist.objects.all()
            money=expenditure.objects.first()
            return render(request,'expenditurehist.html',{'hist':expend,'total':money})
        else:
            # print(m)
            return render(request,'update_expenditure.html')
        
    
    
    
def studentdetails(request):
    students = Student.objects.order_by('-score').values()
    
        
    return render(request,'studentlist.html',{'students':students})

def deletestudent(request,student_id):
    if request.method=="GET":
        Student.objects.get(id=student_id).delete()
        return redirect(studentdetails)

def modifystudent(request,student_id):
    instance = Student.objects.get(id=student_id)
    if request.method == 'POST':
            instance.fullname=request.POST['fullname']
            instance.Grade=request.POST['Grade']
            instance.income=int(request.POST['income'])
            instance.money_needed=request.POST['money_needed']
            if "books" in request.POST:
                instance.books=request.POST['books']
            if "uniform" in request.POST:
                instance.uniform=request.POST['uniform']
            instance.performance=float(request.POST['performance'])
            instance.gender=request.POST['gender']
            instance.__score__()
            instance.save()
            return redirect(studentdetails)
    return render(request,'modifystudent.html',{'instance':instance,'id':student_id})
    