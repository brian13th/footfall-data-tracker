from django.shortcuts import render
from .utils import footfalls_from_csv_to_db, get_chart_type, get_data_to_display,get_yearly_average_footfall
from .models import Footfall
from .forms import SearchForm
from django.contrib import messages

def dashboard_home(request):
    search_form = SearchForm(request.POST or None)
    # footfalls_from_csv_to_db() #run this function if data base is empty to load data
    footfalls = Footfall.objects.all()
    chart = 'bar' # default chart type value
    display = 'raw' # default data to display
    footsteps = None
    dates = None
    mean = None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        display = request.POST.get('display_chart_by')
        footfalls_qs = Footfall.objects.filter(time__date__gte=date_from, time__date__lte=date_to)

        if len(footfalls_qs)>0:
            messages.success(request, "successful submission!")
            footfalls = get_data_to_display(footfalls_qs, display)
            if display == 'normalize':
                footsteps = footfalls['footsteps_normalized'].to_list()
                dates = footfalls['time'].to_list()
                mean = get_yearly_average_footfall(footsteps)
            else:
                mean = get_yearly_average_footfall(footfalls_qs)
            chart = get_chart_type(chart_type)
        else:
            messages.warning(request, 'No data within the dates you provided.. Try again')

    context = {'footfalls':footfalls,
               'search_form':search_form,
               'chart':chart,
               'display':display,
               'footsteps':footsteps,
               'dates':dates,
               'mean':mean}
    return render(request, 'footfalls/dashboard-home.html', context)