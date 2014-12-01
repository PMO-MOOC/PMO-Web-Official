from django.conf.urls import patterns, url

from submit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='submit'),
	
	url(r'^(?P<group_id>\d+)/$', views.detail, name='detail'),
	url(r'^list/$', views.list, name='list'),
	
	#url(r'^add/$', views.index, name='index'),
)