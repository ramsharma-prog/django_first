from django.shortcuts import render

# imports for the registration page
from django.contrib.auth.models import User
from app_six.forms import UserForm, UserProfileInfoForm

# imports for the login & logout page
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# registration page

def index(request):
    index_key = {'index_me': 'I am in the index function from views.py'}
    return render(request, 'app_six/index.html', context = index_key)

    #-----------LOGOUT function----------#
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in sucessfully.")


def base(request):
    base_key = {'base_me': 'I am in the base function from views.py'}
    return render(request, 'app_six/base.html', context = base_key)

def register(request):
        registered = False

        if request.method == "POST":
            # directly from the User module insdie forms.py
            user_form = UserForm(data=request.POST)
            #  belongs to models.py (UserProfileInfo) & imported to forms.py
            profile_form = UserProfileInfoForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save() # grab the UserForm & save it the databse
                user.set_password(user.password) # Hashing the password
                user.save() # Saving the password/changes to the database

                #  belongs to models.py (UserProfileInfo) & imported to forms.py
                profile = profile_form.save(commit=False)

                # profile.user means the class UserProfileInfoForm belongs to..
                #..UserProfileInfo which has the user instance that..
                # equal to the user which is the instance of UserForm/User module
                profile.user = user

                # To check if the user has uploaded the picture..
                # ..profile_pic is a variable to pics in models.py &..
                # ..rest of ot is the special function.
                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']

                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()


        return render(request, 'app_six/registration.html',
                     context = {'user_form': user_form,
                     'profile_form': profile_form,
                     'registered': registered})




def user_login(request):
    if request.method == "POST":
        # getting details from the html login page, inside the label tag such..
        #..as "username", "password".
        username = request.POST.get("username")
        password = request.POST.get('password')
        # django bulid in - authenticates with the following code.
        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account is not active")

        else:
            print(f"username: {username} or password: {password} is not recognised")
            return HttpResponse("Invalid login details")

    else:
        return render(request,'app_six/login.html', {})
