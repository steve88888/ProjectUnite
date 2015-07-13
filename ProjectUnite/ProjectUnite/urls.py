"""projectUnite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	url(r'^$', 'profiles.views.home', name='home'),
    url(r'^myProjects/$', 'projects.views.my_projects', name='my_projects'),
	url(r'^contact/$', 'profiles.views.contact', name='contact'),
	url(r'^edit/$', 'profiles.views.edit_profile', name='edit_profile'),
	url(r'^projectlist/$', 'projects.views.projectlist', name='projectlist'),
    url(r'^newProject/$', 'projects.views.newProject', name='newProject'),
    url(r'^all/$', 'profiles.views.all', name='all'),
	#url(r'^about/$', 'ProjectUnite.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/(?P<projectID>\w+)/$','projects.views.single_project', name = 'single_project'),
    url(r'^members/(?P<username>\w+)/$','profiles.views.single_user', name = 'single_user'),
    url(r'^accounts/', include('registration.backends.default.urls')),
] 
if settings.DEBUG:
	urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)