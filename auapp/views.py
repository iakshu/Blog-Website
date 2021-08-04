from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from django.contrib.auth import login, logout, authenticate
from main_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

def user_signup(request):
	if request.method =="POST":
		email = request.POST.get("email")
		try:
			username = User.objects.get(email=email.lower()).username
			usr = User.objects.get(username=username)
			return render(request,"register.html",{"msg":"Email already registered."})
		except User.DoesNotExist:
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			sub = "welcome to blogapp"
			msg = "ur password is " + str(pw)
			sender = EMAIL_HOST_USER
			rvr = [str(email)]
			send_mail(sub, msg, sender, rvr)
			usr = User.objects.create_user(username=email, password=pw, email=email)
			usr.save()
			return redirect("user_login")
	else:
		return render(request,"register.html")

def user_login(request):
	if request.method =="POST":
		email = request.POST.get("email")
		pw = request.POST.get("pw")
		username = User.objects.get(email=email.lower()).username
		usr = authenticate(username=username, password=pw)
		if usr is None:
			return render(request,"login.html",{"msg":"invalid login"})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"login.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def editprofile(request):
	if not request.user.is_authenticated:
		return redirect("user_login")

	profile = User.objects.get(username = request.user.username)
	form = UserUpdateForm(request.POST, instance = profile)
	
	if request.method == "POST":
		form = UserUpdateForm(request.POST, instance = request.user)

		if form.is_valid():
			form.save()
		else:
			print(form.errors)
	else:
		form = UserUpdateForm(instance = request.user)

	context = {
		"profile":  profile,
		"form": form,
	}
	return render(request, "edit-profile.html", context)


# def user_np(request):
# 	if request.method =="POST":
		
# 		un = request.POST.get("un")
# 		try:
			
# 			usr = User.objects.get(username=un) 
# 			pw = ""
# 			text = "abcdefghijklmnopqrstuvwxyz123456789"
# 			for i in range(6):
# 				pw = pw + text[randrange(len(text))]
# 			print(pw)
# 			sub = "welcome to blogapp"
# 			msg = "your new password is " + str(pw)
# 			sender = EMAIL_HOST_USER
# 			rvr = [str(un)]
# 			send_mail(sub, msg, sender, rvr)
# 			usr.set_password(pw) 
# 			usr.save()
# 			return redirect("user_login")
# 		except User.DoesNotExist:
# 			return render(request,"user_signup.html",{"msg":"email not registered "})
		
# 	else:
# 		return render(request,"user_np.html")
