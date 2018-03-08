from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Save the profile picture if provided by the user
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()

            registered = True

        # When either or both the user_form or the profile_form are Invalid
        else:
            print(user_form.errors, profile_form.errors)

    # When the request is not 'POST'
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    registration_dict = {'user_form': user_form,
                 'profile_form': profile_form,
                 'registered': registered}

    return render(request, 'basic_app/registration.html', context=registration_dict)

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        # For an authenticated user
        if user:
            # For an active user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else: # An inactive user
                return HttpResponse("ACCOUNT IS NOT ACTIVE")

        # User is not authenticated
        else:
            print("Someone has tried to login and failed!")
            print("Username: {} and Password: {}".format(username, password))

            return HttpResponse("Invalid login details supplied")

    # The request is not Post
    else:
        return render(request, 'basic_app/login.html', {})
