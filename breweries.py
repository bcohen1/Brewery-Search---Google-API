import yaml
from decimal import Decimal
import requests
import pandas as pd
import time

'''keep personal info separate'''
with open('credentials.yaml', 'r') as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)
   
my_addr = doc['my_addr']
api_key = doc['api_key']

'''Generate list of lat-longs to search'''
lat_long = []
my_addr_lat = my_addr.split(',')[0]
my_addr_long = my_addr.split(',')[1].strip()

# 1 degree = 111,320m - shift by 0.2 deg
# 1 mile = 1609.34m

for i in range(0, 3):
    combine = str(my_addr_lat) + ', ' + str(round(Decimal(my_addr_long) - Decimal(i*0.2), 7))
    lat_long.append(combine)

for i in range(0, 3):
    combine = str(round(Decimal(my_addr_lat) - Decimal(0.2), 6)) + ', ' + str(round(Decimal(my_addr_long) - Decimal(i*0.2), 7))
    lat_long.append(combine)

'''search nearby breweries, search radii will overlap to avoid 60 
item API limit and ensure no breweries are missed'''
radius = '25000'
api_base = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

full_data = []

for i in range(len(lat_long)):

    api_str = api_base + 'location=' + lat_long[i] + '&radius=' + radius + '&keyword=brewery' + '&key=' + api_key
    api_resp = requests.get(api_str).json()
    json_resp = api_resp['results']
    time.sleep(3)
    
    while 'next_page_token' in api_resp:
        token = api_resp['next_page_token']
        api_str2 = api_base + '&pagetoken=' + token + '&key=' + api_key
        api_resp = requests.get(api_str2).json()
        json_resp.extend(api_resp['results'])
        
    full_data.extend(json_resp)

df = pd.DataFrame(full_data)
df = df[['business_status', 'geometry', 'name', 'opening_hours', 
          'place_id', 'rating', 'user_ratings_total', 'vicinity']]
df.sort_values(by=['rating', 'user_ratings_total'], ascending=False, inplace=True)
df.drop(df[df['business_status'] != 'OPERATIONAL'].index, inplace=True)
df.drop_duplicates(subset=['name'], inplace=True)
df.reset_index(drop=True, inplace=True)
df.drop_duplicates(subset=['name'], inplace=True)
df['vicinity'] = df['vicinity'].str.replace('#', '')
 
dist_api_base = 'https://maps.googleapis.com/maps/api/directions/json?'
dists = []
durations = []

'''get distance and driving time from home'''
for i in df['vicinity']:
    dist_api_str = dist_api_base + 'origin=' + lat_long[0] + '&destination=' + i + '&key=' + api_key
    dist_api_resp = requests.get(dist_api_str).json()
    dist = dist_api_resp['routes'][0]['legs'][0]['distance']['value']
    dists.append(dist)
    duration = dist_api_resp['routes'][0]['legs'][0]['duration']['text']
    durations.append(duration)

df['distance'] = dists
df['duration'] = durations
