import pandas as pd
from .models import Footfall
import datetime

def footfalls_from_csv_to_db():
    Footfall.objects.all().delete()
    footfall_df = pd.read_csv('Footfall.csv', sep=';')
    pd.to_datetime(footfall_df['Time'])
    footfall_records = footfall_df.to_records()

    for record in footfall_records:
        footfall = Footfall.objects.create(time=datetime.datetime.strptime(record[1][0:10],"%Y-%m-%d"), footsteps=int(record[2]))
        footfall.save()

def get_chart_type(chart_type):
    if chart_type == '#1':
        return 'bar'
    elif chart_type == '#2':
        return 'line'
    else:
        print('ups... failed to identify the chart type')
        return None

def get_data_to_display(data, data_type):
    if data_type == 'raw':
        return data
    elif data_type == 'normalize':
        data_df = pd.DataFrame(data.values())
        data_df['footsteps_normalized'] = (data_df['footsteps'] / data_df['footsteps'].max() * 100).round(decimals=2)
        return data_df