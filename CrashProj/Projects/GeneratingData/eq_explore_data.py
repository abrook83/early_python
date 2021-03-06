import json     # import json module

from plotly.graph_objs import Scattergeo, Layout    # 'Scattergeo' chart type
from plotly import offline      # 'offline' moduule to render the map

# explore the structure of the data
filename = 'CrashProj\Projects\data\mapping_global_data_sets\data\eq_data_30_day_m1.json'

with open(filename) as f:   # open and refer to as 'f'
    all_eq_data = json.load(f)     # converts the data into a python-usable format (in this case a dictionary)

all_eq_dicts = all_eq_data['features']      # take 'features' data from the file

mags, lons, lats, hover_texts = [], [], [], []       # empty list of magnitudes, lons, lats....
for eq_dict in all_eq_dicts:        # for all the entries in 'all_eq_dicts'...
    mag = eq_dict['properties']['mag']      # the variable 'mag' is under 'properties', 'mag'
    lon = eq_dict['geometry']['coordinates'][0]     # under 'geometry', 'coords', first entry
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)        # add the value to the list of 'mags'
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)        

print(mags[:10])        # print the first 10
print(lons[:5])
print(lats[:5])

# map the earthquakes (two different ways):
# data = [Scattergeo(lon=lons, lat=lats)]     # create Scattergeo object and feed lats & longs lists...

data = [{                                     # alternate method for the above
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {             # specify the parameters for each marker
        'size': [5*mag for mag in mags],        # creates loc markers dependent on quake magnitude
        'color': mags,      # data to use to scale color against
        'colorscale': 'Electric',    # colour range
        'reversescale': True,       # sets light colour for lightest magnitude....
        'colorbar': {'title': 'Magnitude'}      # generate a scale colourbar, with title 'Magnitude'
    }
}]

my_layout = Layout(title='Global Earthquakes')  # feed info to 'Layout' for title etc.

fig = {'data': data, 'layout': my_layout}       # dictionary contains the data to be fed to the plot
offline.plot(fig, filename='global_earthquakes.html')

readable_file = 'CrashProj\Projects\data/readable_eq_data.json'    # create a readable file to dump the data into
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)     # writes the data into the new file