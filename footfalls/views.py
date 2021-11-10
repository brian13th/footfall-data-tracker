from django.shortcuts import render
from .utils import footfalls_from_csv_to_db, get_chart_type, get_data_to_display
from .models import Footfall
from .forms import SearchForm
# Create your views here.

def dashboard_home(request):
    search_form = SearchForm(request.POST or None)
    footfalls_from_csv_to_db()
    footfalls = Footfall.objects.all()
    chart = 'bar' # default chart type value
    display = 'raw' # default data to display
    footsteps = None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        display = request.POST.get('display_chart_by')

        footfalls_qs = Footfall.objects.filter(time__date__gte=date_from, time__date__lte=date_to)
        footfalls = get_data_to_display(footfalls_qs, display)
        if display == 'normalize':
            footsteps = footfalls['footsteps_normalized'].to_list()
        chart = get_chart_type(chart_type)

    context = {'footfalls':footfalls,
               'search_form':search_form,
               'chart':chart,
               'display':display,
               'footsteps':footsteps,}
    return render(request, 'footfalls/dashboard-home.html', context)