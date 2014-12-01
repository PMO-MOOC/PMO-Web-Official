from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from submit.models import Groups, Partners
from django.template import RequestContext
from django.core.files.base import ContentFile
from django.core.files import File
from submit.forms import UploadFileForm





def index(request):
	#groups = Groups.objects.all()
	#return render(request, 'submit/form.html', {'groups':groups})
	
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			#r = Groups(docfile = request.FILES['file_id'])
			#r.save()
			
			r = Groups(group_name=request.POST['projName'],summary=request.POST['summary'],src_url=request.POST['srcurl'],doc_url=request.POST['docurl'],docfile = request.FILES['file_id'],sub_date=request.POST['date2'])
			r.save()
			#a = Partners(partner_name=request.POST['p1'],group=r)
			#a.save()
			#b= Partners(partner_name=request.POST['p2'],group=r)
			#b.save()
			#c= Partners(partner_name=request.POST['p3'],group=r)
			#c.save()
			
			
			 
		
			#return render_to_response(request, 'submit/result.html', {'r': r})
			#return render_to_response(request, 'submit/result.html',{'form':form})
			#return HttpResponse("Form has been submitted")
			return render(request,'PMO/user_home.html',{'submitted':"Form submitted successfully"})
	else:
		form = UploadFileForm()
 
		data = {'form': form}
		return render_to_response('submit/form.html', data, context_instance=RequestContext(request))



def detail(request, group_id):
	form = DocumentForm()
	doc = Groups.objects.get(pk=group_id)
	return render_to_response(
        'submit/result.html',
        {'doc': doc, 'form': form},
        context_instance=RequestContext(request)
    )

def list(request):
	projects = Groups.objects.all()
	return render_to_response('submit/list.html',{'projects':projects})
    



def add(request):
	
	r = Groups(group_name=request.POST['projName'],summary=request.POST['summary'],src_url=request.POST['srcurl'],doc_url=request.POST['docurl'])
	r.save()
	a = Partners(partner_name=request.POST['p1'],group=r)
	a.save()
	b= Partners(partner_name=request.POST['p2'],group=r)
	b.save()
	c= Partners(partner_name=request.POST['p3'],group=r)
	c.save()
	
	

	
	return render(request, 'submit/result.html', {'r': r})
	
	