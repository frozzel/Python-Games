import requests


response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_position = (latitude, longitude)
    
print(f'Latitude: {latitude}')
print(f'Longitude: {longitude}')
                    
sunrise_sunset_api = 'https://api.sunrise-sunset.org/json'
parameters = {
    'lat': latitude,
    'lng': longitude,
    'formatted': 0,
}

sun_response = requests.get(url=sunrise_sunset_api, params=parameters)
sun_response.raise_for_status()

print(sun_response.json()["results"]["sunrise"])
print(sun_response.json()["results"]["sunset"])