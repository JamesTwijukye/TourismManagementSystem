from django.shortcuts import render
from loginA.login_validation import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate,hashers
from django.contrib.auth.models import User
from booking.models import FeaturedDestination,HomeImages


# Create your views here.
dest_items = FeaturedDestination.objects.all()
hm_items =HomeImages.objects.all()

def LoginView(request):
    return render(request, 'login.html')


def loginAuth(request):
    if request.method == 'POST':
        form_validation_result = LoginForm(request.POST)

        if form_validation_result.is_valid():
            user_email = form_validation_result.cleaned_data['email']
            user_password = form_validation_result.cleaned_data['password']


            result = authenticate(username = user_email, password=user_password)

            if result is not None:
                login(request, result)
                return render(request, 'home.html', {"items":dest_items,"images":hm_items})

            else:
                messages.error(request, "Authentication failed, check user details and try again !")
                return render(request, 'login.html')

        else:
            print("here !")
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    
    return render(request, 'home.html', {"items":dest_items,"images":hm_items})
    

def SignupView(request):
    return render(request, 'signup.html')
      
def SignupAuth(request):
    if request.method == "POST":
        signup_result = SignUpForm(request.POST)

        if signup_result.is_valid():
            user_name = signup_result.cleaned_data["email"]
            user_password= signup_result.cleaned_data["password"]

            hashed_password = hashers.make_password(user_password)

            new_user = User.objects.create_user(user_name, "", user_password)

            new_user.save()

            print(user_password)
            result = authenticate(username=user_name,password=user_password)

            if result is not None:
                login(request,result)
            else:
                messages.error(request,"login error !")

           
            messages.success(request,"you have registered successfully")
            return render(request, 'home.html', {"items":dest_items,"images":hm_items})
            
        
        else:
            print(signup_result.errors)
            messages.error(request, "Invalid registration details")    
            return render(request,'signup.html')
    return render(request,'signup.html')
    
        
        


    

