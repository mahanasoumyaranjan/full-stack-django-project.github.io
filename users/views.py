from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.



def login(request):
    if request.method == 'POST':
        usern = request.POST.get('usr')
        passw = request.POST.get('pass1')
        # name = 
        # 
        name= User.objects.filter(userName = usern).filter(password=passw)
        # p = User.objects.filter(password = passw).first()
        # if name is not None and p is not None:
        if name.exists():
            # user = authenticate(request , userName = usern , password = passw)
            name.update(logged_in=True)
            # if user is not None:
            messages.success(request , f"welcome {name.first()}")
            return redirect("page")
        else:
                messages.info(request , 'Invalid credential')
                return redirect("login")    
        # else:
        #     messages.info(request,'User doest exist')
        #     return redirect("login")
    else:
        return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        user = User()
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('user_name') and request.POST.get('email') and request.POST.get('pass') and request.POST.get('c_pass') and request.POST.get('gender') and request.POST.get('adress') and request.POST.get('number'):
            user.firstName = request.POST.get('first_name')
            user.lastName = request.POST.get('last_name')
            user.userName = request.POST.get('user_name')
            user.email = request.POST.get('email')
            user.phoneNumber = request.POST.get('number')
            user.address = request.POST.get('adress')
            user.password = request.POST.get('pass')
            user.c_password = request.POST.get('c_pass')
            user.gender = request.POST.get('gender')
            if user.password == user.c_password:
                if User.objects.filter(userName = user.userName).exists():
                    messages.success(request , f"UserName already is there")
                    return render(request , 'registration.html')
                else:
                    user.save()
                    messages.info(request , f"Registration sucessful")
                    return redirect("login")
            else:
                messages.info(request , f"Password miss match")
                return render(request , 'registration.html')
            # try:
            #     # num1 = request.POST.get('pass') 
            #     # num2 = request.POST.get('c_pass')
            #     # if num1
            #     user.firstName = request.POST.get('first_name')
            #     user.lastName = request.POST.get('last_name')
            #     user.userName = request.POST.get('user_name')
            #     user.email = request.POST.get('email')
            #     user.phoneNumber = request.POST.get('number')
            #     user.address = request.POST.get('adress')
            #     user.password = request.POST.get('pass')
            #     user.c_password = request.POST.get('c_pass')
            #     gen = request.POST.get('gender')
            #     if gen== 'm' or gen == 'M':
            #         user.gender = "Male"
            #     elif gen== 'f' or gen == 'F':
            #         user.gender = "Female"
            #     elif gen== 'o' or gen == 'O':
            #         user.gender = "Others"
            #     else:
            #         user.gender='NULL'
            #     user.save()
            #     messages.success(request, "Registration successful.")
            #     return redirect("login")
            # except:
            #     return redirect("registration")
    else:
        return render(request , 'registration.html')

def page(request):
    return render(request, 'page.html')
def logout(request):
    return render(request , 'logout.html')
