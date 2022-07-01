from myphone import number
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

def show(basic_txt, additional_txt):
    if additional_txt:
        print(basic_txt + ': ' + additional_txt)
    else:
        print('Error in finding the ' + basic_txt)

n = phonenumbers.parse(number)
city = geocoder.description_for_number(n, 'en')
show('City', city)
carrier = carrier.name_for_number(n, 'en')
show('Carrier', carrier)
timeZone = timezone.time_zones_for_number(n)
print('Time Zone', str(timeZone)[2:-3])

key = '@todo'
geocoder = OpenCageGeocode(key)
query = str(city)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print('Latitude ', lat)
print('Longitude ', lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.CircleMarker(location=[lat, lng], radius=50, popup=city).add_to(myMap)
folium.Marker([lat, lng], popup=city).add_to(myMap)
myMap.save("mylocation.html")