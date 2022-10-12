import requests
import json
import datetime


MY_LAT = 52.524944
MY_LONG = 13.342992

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    json_data = response.json()

    iss_latitude = float(json_data["iss_position"]["latitude"])
    iss_longitude = float(json_data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and \
        MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True
    else:
        print("It's not")
    
    
def is_night():
    parameters = {
            "lat": MY_LAT,
            "long": MY_LONG,
            "formatted": 0
        }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = data["results"]["sunrise"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    
    sunset = data["results"]["sunset"]
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    
    time_now = datetime.datetime.now().hour
    
    print(sunset_hour, time_now, sunrise_hour)
    if sunset_hour <= time_now or time_now <= sunrise_hour:
        print("it's night")

is_iss_overhead()
is_night()