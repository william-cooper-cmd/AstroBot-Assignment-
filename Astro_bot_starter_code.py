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
from datetime import datetime, timezone
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
    try:
        response = requests.get(url,headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    return response.json().get("items", [])


def print_rooms(rooms):
    for room in rooms:
        print(f"name: {room['title']}, type: {room['type']}")


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

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
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
    try:
        requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
    except requests.RequestException:
        return "Failed to send message"

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = 'https://api.openweathermap.org/geo/1.0/direct'
    params = {
        "q": city,
        "limit": 1,
        "appid": api_key}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return f"{city.title()} was not found"

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "lat": location['lat'],
        "lon": location['lon'],
        "units": 'metric',
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return f"Failed to get weather of {city.title()}"

    weather = response.json()

    return format_weather(weather, city.title())

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

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url, params=None, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return "Failed to get ISS location"

    data = response.json()

    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location['name']

    weather_info = get_weather_by_coords(lat, lon, api_key, place)
    return f"ISS Position (Lat: {lat}, Lon: {lon}) at {datetime.fromtimestamp(data['timestamp'], timezone.utc).astimezone().strftime('%d/%m/%Y %H:%M:%S %Z')}:\n{weather_info}"

def get_weather_by_coords(lat, lon, api_key, location_name=None):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "lat": lat,
        "lon": lon,
        "units": 'metric',
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return "Failed to get weather by coordinates"

    weather = response.json()
    return format_weather(weather, location_name)


def format_weather(weather, location_name=None):
    """Formats the raw weather JSON data into a readable string."""
    country = weather.get('sys', {}).get('country', '')
    location_parts = [part for part in [location_name, country] if part]
    if location_parts:
        place = ", ".join(location_parts)
        prefix = f"Current weather in {place}: "
    else:
        prefix = "Current weather (Open Ocean): "

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
    if not token or not weather_key:
        print("Missing Webex token or Weather API key")
        return

    rooms = get_rooms(token)

    if not rooms:
        print("No rooms found" )
        return

    headers = {"Authorization": f"Bearer {token}",}
    try:
        response = requests.get("https://webexapis.com/v1/people/me", headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        print("Failed to get bots name")
        return

    data = response.json()
    bot_name = data['displayName'].lower()

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            message_text = (message_text or "").lower().strip()

            if message_text.startswith(f"{bot_name} /"):
                command = message_text[len(bot_name):].strip()
                cmd, _, arg = command.partition(" ")
                arg = arg.strip()

                if cmd == "/help":
                    send_message(token, room_id, f"@{bot_name} /weather <city>\n@{bot_name} /iss\n@{bot_name} /help\n@{bot_name} /quit")

                elif cmd == "/weather":
                    if not arg:
                        send_message(token, room_id, f"Usage @{bot_name} /weather <city>")
                    else:
                        send_message(token, room_id, get_weather(arg, weather_key))
                elif cmd == "/iss":
                    send_message(token, room_id, get_iss_location(weather_key))
                elif cmd == "/quit":
                    send_message(token, room_id, "AstroBot shutting down.")
                    break
                else:
                    send_message(token, room_id, f"Unknown command. Use @{bot_name} /help")

        time.sleep(5)


if __name__ == '__main__':
    main()
