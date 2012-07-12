from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
#import django.template.RequestContext
from models import *
from forms import *

def home(request):
    return render_to_response('home.html', {"request_user":request.user})

# Django handling the HTTP request.
def example_match(request):
    # Get all the people objects in the data base. candidates is an Array
    candidates = CustomUser.objects.all()

    # Pass all people to the matching algorithm. Get the best match
    the_chosen_one = match(candidates)

    #Pass the best match to the html template and render it to the user
    return render_to_response('match.html', {'chosen_one':the_chosen_one})


# Insert Tran's Matching algorithm here:
def match(*candidates):
    #Pass Mentor list and Mentee list
    for c in candidates:
        print "Do nothing right now"

    return c[0]

def signup(request):
    if request.method == 'POST':
        form = Example_Person_Form(request.POST)
        if form.is_valid():
            new_user = form.save()
            #return render_to_response()
            return HttpResponse("Thank you!")
    else:
        form = Example_Person_Form()

    return render_to_response('signup.html', {'form': form, "request_user":request.user,}, context_instance=RequestContext(request))

def profile(request):
    if request.user.is_authenticated():
        currentUser = CustomUser.objects.filter(id=request.user.id)
        return render_to_response('user_profile.html', {
            'request_user':request.user,
            'currentUser':currentUser,
            })
    else:
        return signup(request)

def logoutUser(request):
    if (request.user.is_authenticated()):
        logout(request)
    return HttpResponseRedirect("/")

def loginUser(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['alias'], password=cd['password'])

            #Authenticate user
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/profile")
        
        #Get user and send to profile page
        #currentUser = CustomUser.objects.filter(username=form['alias'])
        #return render_to_response('user_profile.html', {
        #    'request_user':request.user,
        #    'currentUser':currentUser,
        #    })
    else:
        form = Login()
    return render_to_response('user_login.html', {
        'request_user':request.user,
        'form':form,
        }, context_instance=RequestContext(request))
    
