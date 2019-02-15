from django.shortcuts import render
from UserBasic.forms import UserForm,UserProfileInfoForms

# 

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(req):
	return render(req,'userBasic/index.html')

@login_required
def special(req):
	return HttpResponse("Awsome! You are logged in.")


@login_required
def userlogout(req):
	logout(req)
	return HttpResponseRedirect(reverse('index'))


def register(req):
	registereds = False

	if req.method == "POST":
		user_form = UserForm(data=req.POST)
		profile_form = UserProfileInfoForms(data=req.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user


			if 'profile_pic' in req.FILES:
				profile.profile_pic = req.FILES['profile_pic']

			profile.save()

			registereds = True

		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForms()

	return render(req,'userBasic/registration.html',
								{'user_form':user_form,
								  'profile_form':profile_form,
								   'registered':registereds})

def userlogin(req):
	

	if req.method == 'POST':
		username = req.POST.get('username')
		password = req.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(req,user)

				return render(req,'userBasic/hello.html',{})
				# return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")

		else:
			print("Someone Tried to Login and Failed!!")

			print("Username: {} and password {}".format(username,password))
			return HttpResponse("invalid login credentials!!")

	else:
		return render(req,'userBasic/login.html',{})