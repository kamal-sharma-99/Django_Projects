from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Doctor':
            did = Doctor.objects.get(uid=uid)
            context = {
                'uid': uid,
                'did': did
            }
            return render(request,"myapp/doctor_index.html",context)
        else:
            pid = Patient.objects.get(uid=uid)
            context = {
                'uid': uid,
                'pid': pid
            }
            return render(request,"myapp/patient_index.html",context)
    else:
        return render(request,"myapp/login.html")

def login(request):
    if "email" in request.session:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.POST:
            print("Login Button Clicked")
            email = request.POST['email']
            password = request.POST['password']

            try:
                uid = User.objects.get(email=email,password=password)
                print(uid)
                request.session["email"] = uid.email
                if uid.role == 'Doctor':
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponseRedirect(reverse('home'))
            except:
                e_msg = "Invalid Email or Password"
                return render(request,"myapp/login.html",{'e_msg':e_msg})
        else:
            print("Page Loaded")

        return render(request,"myapp/login.html")

def signup(request):
    if request.POST:
        role = request.POST['role']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        print("------------> role",role)
        print("------------> username",username)
        print("------------> email",email)
        print("------------> contact",contact)
        print("------------> password",password)

        try:
            uid = User.objects.create(email=email, password=password,role=role)
            if role == 'Doctor':
                did = Doctor.objects.create(uid=uid,username=username,contactno=contact)
                if did:
                    s_msg = "Records Added Successfully"
                    return render(request,"myapp/signup.html",{'s_msg':s_msg})
                else:
                    e_msg = "Something Went Wrong ! Please Enter Valid Details"
                    return render(request,"myapp/signup.html",{'e_msg':e_msg})
            else:
                pid = Patient.objects.create(uid=uid,username=username,contactno=contact)
                if pid:
                    s_msg = "Records Added Successfully"
                    return render(request,"myapp/signup.html",{'s_msg':s_msg})
                else:
                    e_msg = "Something Went Wrong ! Please Enter Valid Details"
                    return render(request,"myapp/signup.html",{'e_msg':e_msg})
        except:
            e_msg = "Email Already Exists"
            return render(request,"myapp/signup.html",{'e_msg':e_msg})


    else:
        print("Page Loaded")
        return render(request,"myapp/signup.html")
    


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return HttpResponseRedirect(reverse('login'))
    return render(request,"myapp/login.html")


def doctor_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Doctor':
            did = Doctor.objects.get(uid=uid)
            context = {
                'uid': uid,
                'did': did
            }
            return render(request,"myapp/doctor_profile.html",context)
        
def change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Doctor':
            did = Doctor.objects.get(uid=uid)

            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                del request.session['email']
                s_msg = 'Successfully Password Reset !!'
                return render(request,"myapp/login.html",{'s_msg':s_msg})
            else:
                del request.session['email']
                e_msg = 'You have entered wrong password'
                return render(request,"myapp/login.html",{'e_msg':e_msg})


def doctor_profile_update(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Doctor':
            did = Doctor.objects.get(uid=uid)

            did.username = request.POST['username']
            # did.email = request.POST['email']
            did.contactno = request.POST['contactno']
            did.specification = request.POST['specification']
            did.experience = request.POST['experience']
            did.address = request.POST['address']
            did.visiting_hours = request.POST['visiting_hours']

            did.save()
            context = {
                'uid': uid,
                'did': did
            }
            return render(request,"myapp/doctor_profile.html",context)


def doctors(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Doctor':
            did = Doctor.objects.get(uid=uid)
            context = {
                'uid': uid,
                'did': did
            }
            return render(request,"myapp/doctors.html",context)