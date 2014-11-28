from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from PMO.models import User


def index(request):
	
	if request.method == 'POST':
		r = User(recent_upload = request.POST['anc'],pub_date = request.POST['date1'], user_name = request.POST['user_name'])
		
		r.save()
		#return render(request,'PMO/loggedin.html')
		return render(request,'PMO/user_home.html')
	home = User.objects.order_by('id')
	obj_list = []
	obj_list1 = []
	
	for i in home:
		obj_list.append(i)
		
	obj_list1 = reversed(obj_list) 
	
	d = User.objects.latest('id')	 
				   
	#return render(request, 'PMO/announcement.html',{'home':obj_list1, 'd':d})
	return render(request, 'PMO/index.html',{'home':obj_list1, 'd':d})
	
	
def homepage(request):
	if request.method == 'POST':
		r = User(recent_upload = request.POST['anc'],pub_date = request.POST['date1'], user_name = request.POST['user_name'])
		
		r.save()
		#return render(request,'PMO/loggedin.html')
		return render(request,'PMO/user_home.html')
	#home = User.objects.order_by('id')
	home = User.objects.order_by('pub_date')[5:]
	obj_list = []
	obj_list1 = []
	
	for i in home:
		obj_list.append(i)
		
	obj_list1 = reversed(obj_list) 
	
	d = User.objects.latest('id')	 
				   
	#return render(request, 'PMO/announcement.html',{'home':obj_list1, 'd':d})
	return render(request, 'PMO/PMO.html',{'home':obj_list1, 'd':d})	
	
def archive(request,i_id):
	p = User.objects.get(pk=i_id)
	
	#return HttpResponse(p.recent_upload)
	return render(request, 'PMO/archive.html', {'p':p})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				#return render(request,'PMO/loggedin.html',{'user':user})
				return render(request,'PMO/user_home.html',{'user':user})
				
		else:
				return HttpResponse('User is not valid')		
	else:		
		#return render(request, 'PMO/login.html')
		return render(request, 'PMO/authenticate.html')

def logout_user(request):
	logout(request)
	return render(request,'PMO/authenticate.html')			
	