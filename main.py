from myphone import number
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

def show(basic_txt, additional_txt):
    if additional_txt:
        print(basic_txt + ': ' + additional_txt)
    else:
        print('Error in finding the ' + basic_txt)

n = phonenumbers.parse(number)
location = geocoder.description_for_number(n, 'en')
show('City', location)

service_pro = phonenumbers.parse(number)
show('Service', carrier.name_for_number(service_pro, 'en'))

key = '@todo'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print('Latitude ', lat)
print('Longitude ', lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")
