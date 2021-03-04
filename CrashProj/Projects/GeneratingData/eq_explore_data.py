import json     # import json module

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# explore the structure of the data
filename = 'CrashProj\Projects\data\mapping_global_data_sets\data\eq_data_1_day_m1.json'
with open(filename) as f:   # open and refer to as 'f'
    all_eq_data = json.load(f)     # converts the data into a python-usable format (in this case a dictionary)

all_eq_dicts = all_eq_data['features']      # take 'features' data from the file

mags, lons, lats = [], [], []       # empty list of magnitudes
for eq_dict in all_eq_dicts:        # for all the entries in 'all_eq_dicts'...
    mag = eq_dict['properties']['mag']      # the variable 'mag' is under 'properties', 'mag'
    lon = eq_dict['geometry']['coordinates'][0]     # under 'geometry', 'coords', first entry
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)        # add the value to the list of 'mags'
    lons.append(lon)
    lats.append(lat)        

print(mags[:10])        # print the first 10
print(lons[:5])
print(lats[:5])

# map the earthquakes
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

readable_file = 'CrashProj\Projects\data/readable_eq_data.json'    # create a readable file to dump the data into
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)     # writes the data into the new file