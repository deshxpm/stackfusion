from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from .models import SampleDetail


def home(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		dob = request.POST.get('dob')
		email = request.POST.get('email')
		phone = request.POST.get('phone_number')
		
		email = email.lower()
		obj = SampleDetail.objects.filter(Q(email=email) | Q(name=name) | Q(phone=phone))
		if obj:
			error_msg ="Name or Email or Phone Number already exists! Please try with different!" + '<a href="/">click</a>'
			return HttpResponse(error_msg)
		else:
			save_obj = SampleDetail(name=name, dob=dob, email=email, phone=phone)
			save_obj.save()
			msg= "Successfully Added." + '<a href="/saveddata/">click</a>'
			return HttpResponse(msg)	
	return render(request, 'index.html')



def saveddata(request):
	try:
		data = SampleDetail.objects.all()
	except:
		print("Sorry you have no data!")	
	return render(request, 'detail.html', {'data':data})	