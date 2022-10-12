import requests
import json
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
print(sunrise)
sunrise_hour = sunrise.split("T")[1].split(":")[0]

sunset = data["results"]["sunset"]
print(sunset)
sunset_hour = sunset.split("T")[1].split(":")[0]


print(sunrise_hour, sunset_hour)

time_now = datetime.now()
