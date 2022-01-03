from django.urls import path
from . import views


# point at views.. django will execute it
urlpatterns = [
    path('meetups/', views.index), # our-domain.com/meetups
    path('meetupdetails/', views.meetup_details)
]