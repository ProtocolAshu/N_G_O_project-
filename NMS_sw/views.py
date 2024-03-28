from django.shortcuts import render, HttpResponse
from .models import Student, Donor

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
            donor = Donor.objects.create(name=name, email=email, number=number, password=password)
            donor.save()
            return HttpResponse("Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")
        
            # Proceed with donor registration
            # Add your donor registration logic here

    return render(request, 'register_Donor.html')
def login(request):
    # if request.method == "POST":
    #     # Extract form data
    #     role = request.POST.get("role")
    #     User_id = request.POST.get("user")
    #     Password = request.POST.get("password")
        
    #     try:
    #         myuser = Student.objects.create(role=role, user=User_id, password=Password)
    #         myuser.save()
    #         return HttpResponse("Done Successfully")
    #     except Exception as e:
    #         return HttpResponse(f"Error occurred: {e}")
        
    #         # Proceed with user login
    #         # Add your login logic here

    return render(request, 'login.html')

def eligibility(request):
    return render(request, 'eligibility.html')

def renewal(request):
    # if request.method == "POST":
    #     # Extract form data
    #     F_name = request.POST.get("name")
    #     User_id = request.POST.get("userId")
    #     File_upload = request.FILES.get("fileUpload")
        
    #     try:
    #         myuser = Student.objects.create(name=F_name, userId=User_id, fileUpload=File_upload)
    #         myuser.save()
    #         return HttpResponse("Done Successfully")
    #     except Exception as e:
    #         return HttpResponse(f"Error occurred: {e}")

    #         # Proceed with renewal process
    #         # Add your renewal logic here

     return render(request, 'renewal.html')

def application(request):
    return render(request, 'application.html')

def apply_fresh(request):
    if request.method == "POST":
        F_name = request.POST.get("fullName")
        Gender = request.POST.get("gender")
        Age = request.POST.get("age")
        Class = request.POST.get("class")
        S_name = request.POST.get("schoolName")
        Performance = request.FILES.get("performanceCard")
        G_name = request.POST.get("guardianName")
        F_income = request.POST.get("income")
        Password = request.POST.get("password")
        C_password = request.POST.get("confirmPassword")

        if Password != C_password:
            return render(request, 'apply_fresh.html', {'error_message': 'Both Passwords Do Not Match'})

        try:
            student = Student.objects.create(
                full_name=F_name,
                gender=Gender,
                age=Age,
                class_field=Class,
                school_name=S_name,
                performance_card=Performance,
                guardian_name=G_name,
                income=F_income,
                password=Password
            )

            student.save()
            return HttpResponse("Registration Done Successfully")
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")

    return render(request, 'apply_fresh.html')
