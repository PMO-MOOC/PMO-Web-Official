from django.conf.urls import patterns, url

from PMO import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	 url(r'^groups/$', views.homepage, name='groups'),
	 url(r'^(?P<i_id>\d+)/$', views.archive, name='archive'),
	 url(r'^login/$', views.login_user, name='login_user'),
	url(r'^logout/$', views.logout_user, name='logout_user'),	
	
)