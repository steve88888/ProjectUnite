from django.shortcuts import render, RequestContext, render_to_response, Http404
from .forms import ContactForm, SignUpForm, UserPictureForm
from django.contrib.auth.models import User
from .models import SignUp, UserPicture


#@login_required
def edit_profile(request):
	user = request.user
	signup = SignUp.objects.get(user=user)
	picture = UserPicture.objects.get(user=user)
	signup_form = SignUpForm(request.POST or None, prefix = 'signup', instance = signup)
	user_picture_form = UserPictureForm(request.POST or None, prefix = 'pic', instance = picture)
	

	if signup_form.is_valid() and user_picture_form.is_valid():
		form1 = signup_form.save(commit=False)
		form1.save()
		form2 = user_picture_form.save(commit =False)
		form2.save()




	return render_to_response("update_profile.html", locals(), context_instance=RequestContext(request))


	#if request.user.is_authenticated():
	#	user = request.user	
	#	title = "Welcome to Project Unite"
	#	form = SignUpForm()
	#	picture = UserPictureForm
	
	#	signup = SignUp.objects.get(user = user):
	#	form = SignUpForm(request.POST or None, instance = signup)
	#	picture = UserPicture.objects.get(user = user)
	#	UserPic = UserPictureForm(request.POST or None, request.FILES, instance = picture)

			#if form.is_valid() and UserPic.is_valid():
			#	form1 = form.save(commit = False)
			#	form1.save()
			#	form2 = UserPic.save(commit = False)
			#	form2.save()
		#else:
		#	if request.method=="POST":
	#
	#			context = {
	#			"title": title,
	#			"form": form
	#			}
	#			if form.is_valid():
	#				instance = form.save(commit=False)
	#				instance.save()
	#			return render(request, "update_profile.html", context)
		#"UserPicture": UserPicture
		#}
		#if request.user.is_authenticated():
		#	title = "Project Unite %s" %(request.user)
		
	
		#may require futher validation at a later date
		#if form.is_valid():
		#	instance = form.save(commit=False)
		#	full_name = form.cleaned_data.get("full_name")

			#if not full_name:
			#	full_name = "Unknown Name"
			#	instance.full_name = full_name
			#instance.save()
			#context = {"title": "Your profile has been updated"}
	#return render_to_response("update_profile.html", locals(), context_instance=RequestContext(request))
	#else:
		#title = "Error you must be logged in to update your profile"
		#context = {
		#"title": title
		#}
		#return render(request, "error.html", context)

# Create your views here.
#cant save so use model
def contact(request):
	form = ContactForm(request.POST or None)

	context = {
		"form": form,
	}
	return render(request, "forms.html", context)

def home(request):

	return render(request, "home.html", {})

def all(request):
	if request.user.is_authenticated():
		#for search function!!!!
		users = User.objects.filter(is_active=True)

		return render_to_response('all.html', locals(), context_instance = RequestContext(request))
	else:
		title = "Error you must be logged in to update your profile"
		context = {
		"title": title
		}
		return render(request, "error.html", context)

def single_user(request, username):
	try:
		user = User.objects.get(username=username)
		#name = single_user.get('full_name')
		if user.is_active:
			single_user = user
			model = SignUp
		
	except:
		raise Http404
	#return render(request, "single_user.html", context)
	return render_to_response('single_user.html', locals(), context_instance = RequestContext(request))


