from django.shortcuts import render

# Create your views here.

def home(request):
	template = 'home.html'
	context = locals() #Anything in function of home
	# print settings.BASE_DIR
	return render(request, template, context)

def about(request):
	template = 'about.html'
	context = locals()
	return render(request, template, context)
