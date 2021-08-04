from django.shortcuts import render,redirect
from .forms import BgForm
from .models import BgModel
from django.views.generic import ListView, DetailView

def home(request):
	user = request.user
	posts = BgModel.objects.all()

	context = {
		"posts":posts,
		"user":user,
	}
	return render(request,"home.html",context)

def addpost(request):
	if request.user.is_authenticated:
		if request.method == "POST":			
			fm = BgForm(request.POST)
			if fm.is_valid():
				fm.save()
				return redirect("home")
			return render(request,"addpost.html",{"fm":fm})
			
		else:
			fm = BgForm()
			return render(request,"addpost.html",{"fm":fm})
	else:
		return redirect("user_login")

def blogpage(request, pk):
	user = request.user
	post = BgModel.objects.get(pk = pk)
	context = {
		"post":post,
		"user":user,
	}	
	
	return render(request,"single.html",context)

def update(request, pk):
	if not request.user.is_authenticated:
		return redirect("user_login")
		
	post = BgModel.objects.get(pk = pk)
	fm = BgForm(request.POST or None, instance=post)

	if request.method == "POST":		
		fm = BgForm(request.POST or None, instance=post)
		if fm.is_valid():
			
			fm.save()
			return redirect("home")
		else:
			print(fm.errors)
	else:
		fm = BgForm(instance=post)
	
	context = {
		"fm": fm,
		"post": post,
	} 
	return render(request, "update.html", context)


def deletepost(request, pk):
	post = BgModel.objects.get(pk = pk)	
	post.delete()
	return redirect("home")
	
	
	