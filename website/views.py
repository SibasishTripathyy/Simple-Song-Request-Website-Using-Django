from django.shortcuts import render, HttpResponse
from datetime import datetime
from website.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'index.html')
	# return HttpResponse("This is home page")

def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		contact = Contact(name=name, email=email, message=message, date=datetime.today())
		contact.save()
		messages.success(request, 'Your submission was successful')
	songs = Contact.objects.all().order_by('-id')[:3]
	return render(request, 'contact.html', {'songs': songs})

def submittedContact(request):

	return render(request, 'submittedContact.html')