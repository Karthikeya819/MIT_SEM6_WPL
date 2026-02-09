from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    get_data = {}
    get_data['employees'] = range(10)

    if request.method == "POST":
        format_string = '%Y-%m-%d'
        get_data['date_of_joining'] = request.POST.get('date_of_joining')
        # get_data['result'] = get_data['date_of_joining']
        joining_date = datetime.datetime.strptime(get_data['date_of_joining'], "%Y-%m-%d").date()
        today = datetime.date.today()
        get_data['result'] = 'Yes' if (today - joining_date).days // 365 > 5 else 'No'
    return render(request, 'form.html', get_data)
