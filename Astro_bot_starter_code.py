#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design.  Further step-by-step instructions can be found in the appendix A of this assignment brief.
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach 
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step-by-step development process.
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
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("items", [])
    except (requests.RequestException, ValueError, AttributeError):
        return []

def print_rooms(rooms):
    for room in rooms:
        print(f"name: {room.get('title', 'Unknown')}, type: {room.get('type', 'Unknown')}")


def select_room(rooms):
    while True:
        name = input("Enter room name: ")
        for room in rooms:
            if name.lower() in room.get("title", "").lower():
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
        data = response.json().get("items", [])
    except (requests.RequestException, ValueError, AttributeError):
        return None, None

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
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return False

    return True

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
        data = response.json()
    except (requests.RequestException, ValueError, AttributeError):
        return None

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
        weather = response.json()
    except (requests.RequestException, ValueError):
        return f"Failed to get weather of {city.title()}"

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
        data = response.json()
    except (requests.RequestException, ValueError):
        return None
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        lat = data["iss_position"]["latitude"]
        lon = data["iss_position"]["longitude"]
        timestamp = data["timestamp"]
        iss_time = (
            datetime.fromtimestamp(timestamp, timezone.utc)
            .astimezone()
            .strftime('%d/%m/%Y %H:%M:%S %Z')
        )
    except (requests.RequestException, KeyError, TypeError, ValueError, OverflowError, OSError):
        return "Failed to get ISS location"


    place = "Over Ocean / No Nearby City"

    location = reverse_geocode(lat, lon, api_key)
    if location:
        place = location.get('name', place)

    weather_info = get_weather_by_coords(lat, lon, api_key, place)
    return f"ISS Position (Lat: {lat}, Lon: {lon}) at {iss_time}:\n{weather_info}"

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
        weather = response.json()
    except (requests.RequestException, ValueError):
        return "Failed to get weather by coordinates"

    return format_weather(weather, location_name)



def format_weather(weather, location_name=None):
    country = weather.get('sys', {}).get('country', '')
    location_parts = [part for part in [location_name, country] if part]
    if location_parts:
        place = ", ".join(location_parts)
        prefix = f"Current weather in {place}: "
    else:
        prefix = "Current weather (Open Ocean): "

    clouds = weather.get('clouds', {}).get('all')
    visibility = weather.get('visibility')
    humidity = weather.get('main', {}).get('humidity')
    wind_speed = weather.get('wind', {}).get('speed')
    temp = weather.get('main', {}).get('temp')
    desc = (weather.get('weather') or [{}])[0].get('description')

    readings = [clouds, visibility, humidity, wind_speed]
    is_good_stargazing = (
            None not in readings and
            clouds <= 15 and
            visibility >= 10000 and
            humidity < 60 and
            wind_speed < 5
    )
    stargazing_status = "Good for stargazing" if is_good_stargazing else "Not good for stargazing"

    temp_text = f"{temp}°C" if temp is not None else "N/A"
    desc_text = desc if desc else "Unknown"
    humidity_text = f"{humidity}%" if humidity is not None else "N/A"
    wind_text = f"{wind_speed} m/s" if wind_speed is not None else "N/A"

    return (
        f"{prefix}"
        f"{temp_text}, {desc_text} | "
        f"humidity: {humidity_text}, "
        f"wind speed: {wind_text}. "
        f"{stargazing_status}"
    )

# =========================
# LAUNCH FUNCTIONS
# =========================

LAUNCH_CACHE = {"time": 0, "text": None}
LAUNCH_CACHE_SECONDS = 600

def format_launch(launch):
    name = launch.get("name", "Unknown launch")
    provider = (launch.get("launch_service_provider") or {}).get("name", "Unknown provider")

    pad = launch.get("pad") or {}
    pad_name = pad.get("name", "Unknown pad")
    location = (pad.get("location") or {}).get("name", "")
    place = f"{pad_name}, {location}" if location else pad_name

    try:
        when = datetime.fromisoformat(launch["net"].replace("Z", "+00:00")).astimezone().strftime('%d/%m/%Y %H:%M %Z')
    except (KeyError, AttributeError, ValueError):
        when = "TBD"

    return (
        f"{name}\n"
        f"When (NET): {when}\n"
        f"Provider: {provider}\n"
        f"Pad: {place}"
    )

def get_upcoming_launches():
    now = time.time()
    if LAUNCH_CACHE["text"] and now - LAUNCH_CACHE["time"] < LAUNCH_CACHE_SECONDS:
        return LAUNCH_CACHE["text"]

    url = "https://ll.thespacedevs.com/2.3.0/launches/upcoming/"
    params = {"limit": 5}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        results = response.json().get("results", [])
    except (requests.RequestException, ValueError, AttributeError):
        if LAUNCH_CACHE["text"]:
            return LAUNCH_CACHE["text"] + "\n(Live update failed, showing cached data)"
        return "Failed to get upcoming launches (the API may be rate limited, try again later)"

    if not results:
        return "No upcoming launches found"

    text = "Upcoming rocket launches:\n\n" + "\n\n".join(format_launch(i) for i in results)

    LAUNCH_CACHE["time"] = now
    LAUNCH_CACHE["text"] = text
    return text

# =========================
# MAIN BOT LOGIC
# =========================

def handle_command(cmd, arg, bot_name, weather_key):
    """Run one bot command and return (reply_text, should_quit)."""
    if cmd == "/help":
        return (
            f"@{bot_name} /weather <city>\n"
            f"@{bot_name} /iss\n"
            f"@{bot_name} /launch\n"
            f"@{bot_name} /help\n"
            f"@{bot_name} /quit"
        ), False

    if cmd == "/weather":
        if not arg:
            return f"Usage: @{bot_name} /weather <city>", False
        return get_weather(arg, weather_key), False

    if cmd == "/iss":
        return get_iss_location(weather_key), False

    if cmd == "/launch":
        return get_upcoming_launches(), False

    if cmd == "/quit":
        return "AstroBot shutting down.", True

    return f"Unknown command. Use @{bot_name} /help", False

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

    bot_name = get_bot_name(token)

    if not bot_name:
        print("Failed to get bot's name")
        return

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

                reply, should_quit = handle_command(cmd, arg, bot_name, weather_key)

                if not send_message(token, room_id, reply):
                    print("Warning: failed to send reply to Webex")

                if should_quit:
                    break

        time.sleep(5)

def get_bot_name(token):
    url = "https://webexapis.com/v1/people/me"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None

    if not isinstance(data, dict):
        return None

    # split() on an empty or missing name gives an empty list, so check it first
    words = str(data.get("displayName", "")).split(maxsplit=1)
    return words[0].lower() if words else None


if __name__ == '__main__':
    main()
