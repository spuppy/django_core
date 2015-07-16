from django.shortcuts import render

from .forms import ContactForm

def home(request):

	title = "Contact Us!"
	form = ContactForm(request.POST or None)
	comfirm_message = None
	

	if form.is_valid():
		#print request.POST
		print form.cleaned_data['email']

		title='Thank you!'
		comfirm_message='Thank you for your message. We have received it and we are reviewing it'
			
		# Clear form
		form = None

	# print comfirm_message
	context = {
		'title': title,
		'form': form,
		'comfirm_message': comfirm_message
	}
	print comfirm_message
	template = 'contact.html'
	# context = locals()
	return render(request, template, context)