from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"myapp/index.html")

def login(request):
    return render(request,"myapp/login.html")

def signup(request):
    if request.POST:
        role = request.POST['role']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        print("------------> role",role)
        print("------------> username",username)
        print("------------> email",email)
        print("------------> contact",contact)
        return render(request,"myapp/signup.html")
    else:
        print("Page Loaded")
        return render(request,"myapp/signup.html")