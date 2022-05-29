from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import *

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def art_of_day(request):
    date = dt.date.today()
    art = Pic.todays_art()
    locations = Location.objects.all()
    return render(request, 'all-art/today-art.html', {"date": date, "art": art,"locations": locations})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    art = Pic.objects.filter(location = selected_location.id)
    return render(request, 'all-art/location.html', {"location":selected_location,"locations":locations,"art":art})    



def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def art_today(request):
    date = dt.date.today()
    art = Pic.todays_art()
    return render(request, 'all-art/today-art.html', {"date": date,"art":art})

def search_results(request):

    if 'pics' in request.GET and request.GET["pics"]:
        search_term = request.GET.get("pics")
        searched_pics = Pic.search_by_category(search_term)
        message = f"{search_term}"
        category = Category.objects.all()
        context = {
            "category":category,
            "message":message,
            "pics":searched_pics
        }

        return render(request, 'all-art/search.html',{"message":message,"pics": searched_pics, category: "category"})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-art/search.html',{"message":message})

