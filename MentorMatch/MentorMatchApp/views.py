from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
#import django.template.RequestContext
from models import *
from forms import *

# Django handling the HTTP request.
def example_match(request):
    # Get all the people objects in the data base. candidates is an Array
    candidates = ExamplePerson.objects.all()

    # Pass all people to the matching algorithm. Get the best match
    the_chosen_one = match(candidates)

    #Pass the best match to the html template and render it to the user
    return render_to_response('match.html', {'chosen_one':the_chosen_one})


# Insert Tran's Matching algorithm here:
def match(*candidates):
    for c in candidates:
        print "Do nothing right now"
        #Super complicated algorithm

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
 
