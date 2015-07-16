from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=120,required=False)
	email = forms.EmailField(required=True,help_text='a valid email address, please')
	comment = forms.CharField(required=True,widget=forms.Textarea)
