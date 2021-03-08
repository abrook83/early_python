import csv
from logging import currentframe

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime

filename = 'Python Crash Course Works\Projects\Datasets\FireData_MODIS_C6_Australia_NewZealand_48h.csv'

with open(filename) as f:
    reader = csv.reader(f)         # pass the open doc into the reader
    header_row = next(reader)       # access the first row

    for index, column_header in enumerate(header_row):      # enumerate gives each list item a number
        print(index, column_header)

# retrieve data from the file
    lats, lons, brightnesses, dates, = [], [], [], []      # empty lists of location & data
    for row in reader:      # for each row in the opened & read file...
        current_date = datetime.strptime(row[5], '%Y-%m-%d')   # date from row 5
        dates.append(current_date)
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        brightnesses.append(float(row[2]))

fire_data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.05*bright for bright in brightnesses],
        'color': brightnesses,
        'colorscale': 'Electric',
        'reversescale': True,
        'colorbar': {'title': 'Fire Brightness'},
    },
}]

my_layout = Layout(title='Global Fires')

fig = {'data': fire_data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

        # try:
        #     exp = float(row[5])  # ...take the 5th column as an float
        # except ValueError:
        #     print(f"Missing data for {current_date}")
        # else:
        #     dates.append(current_date)
        #     exp_lvls.append(exp)  # add it to the list of highs




