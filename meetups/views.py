from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# what happens when the user goes to a url 

from .models import Meetup

def index(request): 
  meetups = Meetup.objects.all
  
  # meetups = [
  #   { 'title': 'A First Meetup'},
  #   { 'title': 'A second Meetup'}
  # ]
  return render(request, 'meetups/index.html', {
      'meetups': meetups,
      'show_meetups': True,
    })

def meetup_details(request):
    selected_meetup = {'title': 'A first Meetup', 'description': 'This is the first meetup!'}
    return render(request, 'meetups/meetup-detail.html',{
      'meetup_title': selected_meetup['title'],
      'meetup_description': selected_meetup['description']

    })