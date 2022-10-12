import json
import requests

def json_scraper(url, file_name):
    print("Start scraping")
    response = requests.get(url)
    json_data = response.json()
    
    # Create json file
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        
    print("End scraping")
    
    longitude = json_data["iss_position"]["longitude"]
    latitude = json_data["iss_position"]["latitude"]
    print(longitude, latitude)
    
if __name__ == "__main__":
    json_scraper("http://api.open-notify.org/iss-now.json","iss_data.json")