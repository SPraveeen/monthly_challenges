from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

monthly_challenges={
    "january":"Eat no meat for this moth !",
    "february":"walk for atleat 20 minutes each day !",
    "march":"Learn Django for 20 minu a day !",
    "april":"Eat no meat for this moth !",
    "may":"walk for atleat 20 minutes each day !",
    "june":"Learn Django for 20 minu a day !",
    "july":"Eat no meat for this moth !",
    "august":"walk for atleat 20 minutes each day !",
    "september":"Learn Django for 20 minu a day !",
    "october":"Eat no meat for this moth !",
    "november":"walk for atleat 20 minutes each day !",
    "december":"Learn Django for 20 minu a day !",
}

# Create your views here.
# view is a function/class

def monthly_challenges_by_number(request,month):
    months=list(monthly_challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("Month invalid")
    
    else:
        redirect_month=months[month-1]
        return HttpResponseRedirect("/challenges/"+redirect_month)

def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
