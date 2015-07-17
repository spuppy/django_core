from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

def home(request):
	template = 'home.html'
	context = {}
	# print settings.BASE_DIR
	return render(request, template, context)

def about(request):
	template = 'about.html'
	context = {}
	return render(request, template, context)

@login_required
def user_profile(request):
	if request.user.is_authenticated:
		user = request.user
	else:
		user = None
	template = 'profile.html'
	context = {'myuser': user}
	return render(request, template, context)