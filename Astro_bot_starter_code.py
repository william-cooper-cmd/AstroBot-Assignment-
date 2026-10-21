#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design.  Further step by step instructions can be found in the appendix A of this assignment brief. 
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach 
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step by stepdevelopment process.
# =========================
# REQUIRED LIBRARIES
# =========================

import requests
import json
import time
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# =========================
# CONFIGURATION FUNCTIONS
# =========================
def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ")
        return token
    else:
        return os.getenv("WEBEX_TOKEN")

def get_api_key(prompt, hardcoded_key):
    choice = input(f"Use hard-coded {prompt}? (y/n): ").lower()
    if choice == "n":
        api_key = input(f"Enter your {prompt}: ")
        return api_key
    else:
        return hardcoded_key

# =========================
# WEBEX FUNCTIONS
# =========================
def get_rooms(token):
    url = "https://webexapis.com/v1/rooms"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url,headers=headers)
    print(response)

    if response.status_code != 200:
        print("Error fetching rooms:", response.status_code)
        return []

    return response.json().get("items", [])


def print_rooms(rooms):
    for room in rooms:
        print(room["id"], room["title"])


def select_room(rooms):
    while True:
        name = input("Enter room name: ")
        for room in rooms:
            if name.lower() in room["title"].lower():
                print(f"selected room is {room['title']}")
                return room["id"]
        print("Selected room not found")


def get_latest_message(token, room_id):
    url = 'https://webexapis.com/v1/messages'
    params = {"roomId":room_id, "max": 1, "mentionedPeople": "me"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None, None

    data = response.json().get("items", [])

    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")


def send_message(token, room_id, message):
    url = 'https://webexapis.com/v1/messages'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "roomId": room_id,
        "text": message
    }
    requests.post(url, headers=headers, data=json.dumps(data))

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = 'https://api.openweathermap.org/geo/1.0/direct'
    params = {
        "q": city,
        "limit": 1,
        "appid": api_key}
    response = requests.get  (url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return f"{city} was not found"

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "lat": location['lat'],
        "lon": location['lon'],
        "units": 'metric',
        "appid": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Failed to get weather for {city}"

    weather = response.json()

    return format_weather(weather, city)

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = "https://api.openweathermap.org/geo/1.0/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "limit": 1,
        "appid": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url, params=None)

    if response.status_code != 200:
        return "Failed to get ISS location"

    data = response.json()

    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location['name']

    weather_info = get_weather_by_coords(lat, lon, api_key, place)
    return f"ISS Position (Lat: {lat}, Lon: {lon}) at {datetime.now().astimezone().strftime("%Z")   }:\n{weather_info}"

def get_weather_by_coords(lat, lon, api_key, location_name=None):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "lat": lat,
        "lon": lon,
        "units": 'metric',
        "appid": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Failed to get weather for coordinates ({lat}, {lon})"

    weather = response.json()
    return format_weather(weather, location_name)


def format_weather(weather, location_name=None):
    """Formats the raw weather JSON data into a readable string."""
    country = weather.get('sys', {}).get('country', '')
    prefix = f"Current weather in {location_name}, {country}: " if location_name else f"Current weather: "

    is_good_stargazing = (
        weather['clouds']['all'] <= 15 and
        weather['visibility'] >= 10000 and
        weather['main']['humidity'] < 60 and
        weather['wind']['speed'] < 5
    )
    stargazing_status = "Good for stargazing" if is_good_stargazing else "Not good for stargazing"

    return (
        f"{prefix}"
        f"{weather['main']['temp']}°C, {weather['weather'][0]['description']} | "
        f"humidity: {weather['main']['humidity']}%, "
        f"wind speed: {weather['wind']['speed']} m/s. "
        f"{stargazing_status}"
    )

# =========================
# MAIN BOT LOGIC
# =========================
def main():

    token = get_webex_token()

    weather_key = get_api_key(
        "Weather API key",
        os.getenv("API_KEY")
    )

    rooms = get_rooms(token)

    if not rooms:
        print("No rooms found" )
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print(message_text)

            if not message_text.lower().startswith('astro /'):
                continue

            if message_text.lower() == "astro /help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith('astro /weather'):

                parts = message_text.split(maxsplit=2)

                if len(parts) < 3:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[2]
                    send_message(token, room_id, get_weather(city, weather_key))

            elif message_text.lower() == "astro /iss":
                send_message(token, room_id, get_iss_location(weather_key))

            elif message_text.lower() == "astro /quit":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)


if __name__ == '__main__':
    main()
