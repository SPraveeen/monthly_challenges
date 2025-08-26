from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
# view is a function/class

def monthyly_challenges_by_number(request,month):
    return HttpResponse(month)

def monthly_challenges(request,month):
    challenge_text=None
    if month=="january":
        challenge_text="Eat no meat for this moth !"
    elif month=="february":
        challenge_text="walk for atleat 20 minutes each day !"
    elif month=="march":
        challenge_text="Learn Django for 20 minu a day !"
    else:
        return HttpResponseNotFound("This month is not supported !")
    return HttpResponse(challenge_text)
