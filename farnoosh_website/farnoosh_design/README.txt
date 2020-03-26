-e TODO in farnoosh_design/farnoosh_design/: 
	
 _____________ in farnoosh_design/settings.py,  INSTALLED_APPS list 
	
 __________________________'apps.interior_design', 
	
 _____________ in urls.py:  
	
 __________________________ comment out, or just delete 'from django.contrib import admin'
	
 __________________________url(r'^', include('apps.interior_design.urls')),	# add to url patterns, don't forget the comma 
	TODO in farnoosh_design/appsinterior_design/: 
	
 _____________ in urls.py:
	
 __________________________ from django.conf.urls import url
	
 __________________________ from . import views
	
 __________________________in urlpatterns add
	
 ________________________________________ url(r'^$', views.index), # index is the name of a method in views.py
	
 _____________ in views.py:
	
 __________________________from django.shortcuts import render, redirect
	
 __________________________def index(request):
	
 __________________________    return render(request, 'interior_design/index.html')
