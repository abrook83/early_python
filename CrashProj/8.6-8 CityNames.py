### 8.6 City Names ###

# def city_name(name, country):
#     """ return a city & its country """
#     deets = f"{name}, {country}"
#     return deets

# sant = city_name('santiago', 'chile')
# print(sant.title())


### 8.7 Album ###

def make_album(artist, title):
    """ make a dictionary of aritst / title entries """
    aldeets = {
        'artist': artist.title(),
        'title': title.title(),
    }
    return aldeets

album  = make_album('metallica','ride the lightning')
print(album)