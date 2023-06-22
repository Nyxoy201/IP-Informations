import requests
import pystyle
from pystyle import Colors, Colorate


API_KEY = '992a17286db132530e43b67c002d9dd0'


def localiser_ip(ip):
    url = f'http://api.ipstack.com/{ip}?access_key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pays = data['country_name']
        region = data['region_name']
        ville = data['city']
        code_postal = data['zip']
        latitude = data['latitude']
        longitude = data['longitude']
        type = data['type']
       
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' Country : {pays}'))
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' Region : {region}'))
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' City : {ville}'))
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' Postcode : {code_postal}'))
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' Latitude : {latitude}'))
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' Longitude : {longitude}'))
        print(Colorate.Horizontal(Colors.blue_to_cyan,f' Type : {type}'))
        
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow,'An error occurred during the API request...'))



adresse_ip = input(Colorate.Horizontal(Colors.blue_to_cyan,"""
  ___   ____      ___   _   _   _____    ___    ____  
 |_ _| |  _ \    |_ _| | \ | | |  ___|  / _ \  / ___| 
  | |  | |_) |    | |  |  \| | | |_    | | | | \___ \ 
  | |  |  __/     | |  | |\  | |  _|   | |_| |  ___) |
 |___| |_|       |___| |_| \_| |_|      \___/  |____/ 

                                        BY NYXOY                                  
                                                                
 Enter IP address :"""))
localiser_ip(adresse_ip)

leave = input(Colorate.Horizontal(Colors.blue_to_cyan,"""
 Press any key to exit """))


