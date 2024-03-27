from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()  # Fetch the custom user model (if you have one)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def As_Student(request):
    return render(request, 'As_Student.html')

def register_Donor(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("Number")
        password = request.POST.get("password")
    
        try:
            myuser = User.objects.create_user(name=name,email=email,Number=number, password=password)
            myuser.save()
            return HttpResponse("Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")
        
            # Proceed with donor registration
            # Add your donor registration logic here

    return render(request, 'register_Donor.html')

def login(request):
    if request.method == "POST":
        # Extract form data
        role = request.POST.get("role")
        User_id = request.POST.get("user")
        Password = request.POST.get("password")
        
        try:
            myuser = User.objects.create_user(role=role, user=User_id, password=Password)
            myuser.save()
            return HttpResponse("Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")
        
            # Proceed with user login
            # Add your login logic here

    return render(request, 'login.html')

def eligibility(request):
    return render(request, 'eligibility.html')

def renewal(request):
    if request.method == "POST":
        # Extract form data
        F_name = request.POST.get("name")
        User_id = request.POST.get("userId")
        File_upload = request.FILES.get("fileUpload")
        
        try:
            myuser = User.objects.create_user(name=F_name, userId=User_id, fileUpload=File_upload)
            myuser.save()
            return HttpResponse("Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")

            # Proceed with renewal process
            # Add your renewal logic here

    return render(request, 'renewal.html')

def application(request):
    return render(request, 'application.html')

def apply_fresh(request):
    if request.method=="POST":
        F_name=request.POST.get("fullName")
        Gender=request.POST.get("gender")
        Age=request.POST.get("age")
        Class=request.POST.get("class")
        S_name=request.POST.get("schoolName")
        Performance=request.FILES.get("performanceCard")
        G_name=request.POST.get("guardianName")
        F_income=request.POST.get("income")
        Password=request.POST.get("password")
        C_password=request.POST.get("confirmPassword")
        # print(F_name, Gender, Age, Class, S_name, Performance, G_name, F_income, Password, C_password)

        if Password != C_password:
            return render(request, 'apply_fresh.html', {'error_message': 'Both Passwords Do Not Match'})
        try:
            myuser = User.objects.create_user(fullName=F_name, password=Password, gender=Gender, age=Age, class_field=Class, school_name=S_name, performance_card=Performance, guardian_name=G_name, income=F_income)
            myuser.save()
            return HttpResponse("Registration Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")

    return render(request, 'apply_fresh.html')