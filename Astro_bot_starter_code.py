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

# Read the WEBEX_TOKEN and API_KEY values from the .env file into the environment
load_dotenv()

# =========================
# CONFIGURATION FUNCTIONS
# =========================
def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower()
    if choice == "n":
        # The user typed a token, so it never has to be stored in a file
        token = input("Enter your Webex Access Token: ")
        return token
    else:
        # Any other answer uses the token saved in the .env file (None if missing)
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
    # Webex uses a Bearer token in the Authorization header for every request
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    try:
        # timeout stops the bot hanging forever if the server does not answer
        response = requests.get(url, headers=headers, timeout=10)
        # Raise an error for 4xx/5xx status codes (e.g. 401 for a bad token)
        response.raise_for_status()
        # The rooms are in the "items" list of the JSON response
        return response.json().get("items", [])
    except (requests.RequestException, ValueError, AttributeError):
        # Network error, bad status, invalid JSON or unexpected shape: return no rooms
        return []

def print_rooms(rooms):
    for room in rooms:
        # .get() with a default avoids a crash if a field is missing
        print(f"name: {room.get('title', 'Unknown')}, type: {room.get('type', 'Unknown')}")


def select_room(rooms):
    while True:
        name = input("Enter room name: ")
        for room in rooms:
            # Case-insensitive partial match, so "astro" finds "Astronomy Club"
            if name.lower() in room.get("title", "").lower():
                print(f"selected room is {room['title']}")
                return room["id"]
        # Nothing matched, so the while loop asks again
        print("Selected room not found")


def get_latest_message(token, room_id):
    url = 'https://webexapis.com/v1/messages'
    # max=1 gets only the newest message, and mentionedPeople=me limits results
    # to messages that @mention the bot
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
        # Return a pair so the caller can always unpack two values
        return None, None

    # No messages mentioning the bot yet
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
    # POST body: which room to send to and the message text
    data = {
        "roomId": room_id,
        "text": message
    }
    try:
        # json.dumps converts the Python dictionary into a JSON string
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return False

    # True lets the caller know the reply was delivered
    return True

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = 'https://api.openweathermap.org/geo/1.0/direct'
    # q is the city name, limit=1 returns only the best match
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

    # The API returns a list, which is empty if the city is not found
    return data[0] if data else None

def get_weather(city, api_key):
    # Step 1: convert the city name to latitude and longitude
    location = get_city_coordinates(city, api_key)

    if not location:
        return f"{city.title()} was not found"

    # Step 2: use those coordinates to get the current weather
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "lat": location['lat'],
        "lon": location['lon'],
        "units": 'metric',  # temperatures in degrees Celsius
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
    # The list is empty when the point is over the ocean with no nearby place
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Read the position and time from the JSON response
        lat = data["iss_position"]["latitude"]
        lon = data["iss_position"]["longitude"]
        timestamp = data["timestamp"]
        # Convert the epoch time (seconds since 1970) to local time using the datetime module
        iss_time = (
            datetime.fromtimestamp(timestamp, timezone.utc)
            .astimezone()
            .strftime('%d/%m/%Y %H:%M:%S %Z')
        )
    except (requests.RequestException, KeyError, TypeError, ValueError, OverflowError, OSError):
        # Covers network errors, missing JSON keys and invalid timestamps
        return "Failed to get ISS location"


    # Default name used when the ISS is not near any city
    place = "Over Ocean / No Nearby City"

    # Look up the nearest place name for the ISS coordinates
    location = reverse_geocode(lat, lon, api_key)
    if location:
        place = location.get('name', place)

    # Get the weather at the ISS coordinates and combine it with the position text
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
    # Build the start of the message from the place name and country code
    country = weather.get('sys', {}).get('country', '')
    location_parts = [part for part in [location_name, country] if part]
    if location_parts:
        place = ", ".join(location_parts)
        prefix = f"Current weather in {place}: "
    else:
        prefix = "Current weather (Open Ocean): "

    # Missing values stay as None so they can be displayed as N/A
    clouds = weather.get('clouds', {}).get('all')
    visibility = weather.get('visibility')
    humidity = weather.get('main', {}).get('humidity')
    wind_speed = weather.get('wind', {}).get('speed')
    temp = weather.get('main', {}).get('temp')
    # "weather" is a list, so take its first item (or an empty dict if it is missing)
    desc = (weather.get('weather') or [{}])[0].get('description')

    # Stargazing is only "good" if every reading exists and passes its limit:
    # cloud cover <= 15%, visibility >= 10 km, humidity < 60%, wind < 5 m/s
    readings = [clouds, visibility, humidity, wind_speed]
    is_good_stargazing = (
            None not in readings and
            clouds <= 15 and
            visibility >= 10000 and
            humidity < 60 and
            wind_speed < 5
    )
    stargazing_status = "Good for stargazing" if is_good_stargazing else "Not good for stargazing"

    # Text shown to the user: missing values appear as N/A or Unknown
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

# Launch Library allows only about 15 unauthenticated requests per hour,
# so the formatted result is cached for 10 minutes
LAUNCH_CACHE = {"time": 0, "text": None}
LAUNCH_CACHE_SECONDS = 600

def format_launch(launch):
    # Each value falls back to "Unknown" so a missing field cannot crash the bot
    name = launch.get("name", "Unknown launch")
    provider = (launch.get("launch_service_provider") or {}).get("name", "Unknown provider")

    # The pad has a name and a nested location, e.g. "Pad 39A, Kennedy Space Center"
    pad = launch.get("pad") or {}
    pad_name = pad.get("name", "Unknown pad")
    location = (pad.get("location") or {}).get("name", "")
    place = f"{pad_name}, {location}" if location else pad_name

    # "net" is the no-earlier-than time in UTC, converted here to local time
    try:
        # Python needs "+00:00" instead of "Z" to read the UTC time
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
    # Return the saved text if it is less than 10 minutes old, saving an API call
    now = time.time()
    if LAUNCH_CACHE["text"] and now - LAUNCH_CACHE["time"] < LAUNCH_CACHE_SECONDS:
        return LAUNCH_CACHE["text"]

    url = "https://ll.thespacedevs.com/2.3.0/launches/upcoming/"
    # Ask for only the next 5 launches
    params = {"limit": 5}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        # The launches are in the "results" list of the JSON response
        results = response.json().get("results", [])
    except (requests.RequestException, ValueError, AttributeError):
        # Fall back to older cached data if the live request fails
        if LAUNCH_CACHE["text"]:
            return LAUNCH_CACHE["text"] + "\n(Live update failed, showing cached data)"
        return "Failed to get upcoming launches (the API may be rate limited, try again later)"

    if not results:
        return "No upcoming launches found"

    # Format every launch and join them with a blank line between each
    text = "Upcoming rocket launches:\n\n" + "\n\n".join(format_launch(i) for i in results)

    # Save the result and the time so the next requests can reuse it
    LAUNCH_CACHE["time"] = now
    LAUNCH_CACHE["text"] = text
    return text

# =========================
# MAIN BOT LOGIC
# =========================

def handle_command(cmd, arg, bot_name, weather_key):
    # Only the commands listed here are accepted, so other input is never run
    if cmd == "/help":
        return (
            f"@{bot_name} /weather <city>\n"
            f"@{bot_name} /iss\n"
            f"@{bot_name} /launch\n"
            f"@{bot_name} /help\n"
            f"@{bot_name} /quit"
        ), False

    if cmd == "/weather":
        # A city name is required, so show the usage message if it is missing
        if not arg:
            return f"Usage: @{bot_name} /weather <city>", False
        return get_weather(arg, weather_key), False

    if cmd == "/iss":
        return get_iss_location(weather_key), False

    if cmd == "/launch":
        return get_upcoming_launches(), False

    # True tells main() to stop the polling loop after sending the reply
    if cmd == "/quit":
        return "AstroBot shutting down.", True

    # Anything else is an unknown command
    return f"Unknown command. Use @{bot_name} /help", False

def main():
    # Step 1: get the credentials, either from .env or typed in
    token = get_webex_token()

    weather_key = get_api_key(
        "Weather API key",
        os.getenv("API_KEY")
    )
    # Stop early with a clear message instead of failing later with a 401 error
    if not token or not weather_key:
        print("Missing Webex token or Weather API key")
        return

    # Step 2: list the rooms the bot can see
    rooms = get_rooms(token)

    if not rooms:
        print("No rooms found" )
        return

    # Step 3: find out the bot's name so commands can be matched against it
    bot_name = get_bot_name(token)

    if not bot_name:
        print("Failed to get bot's name")
        return

    # Step 4: let the user choose which room the bot will watch
    print_rooms(rooms)
    room_id = select_room(rooms)

    # Remember the newest message so old commands are not run on startup
    last_message_id, _ = get_latest_message(token, room_id)

    # Step 5: poll the room forever until a /quit command breaks the loop
    while True:

        message_id, message_text = get_latest_message(token, room_id)

        # Only act on a message we have not handled before
        if message_id and message_id != last_message_id:

            last_message_id = message_id

            # Lower-case and trim the text so matching is not case sensitive
            message_text = (message_text or "").lower().strip()

            # Commands look like "<bot name> /command argument"
            if message_text.startswith(f"{bot_name} /"):
                # Remove the bot name, then split into the command and its argument
                command = message_text[len(bot_name):].strip()
                cmd, _, arg = command.partition(" ")
                arg = arg.strip()

                reply, should_quit = handle_command(cmd, arg, bot_name, weather_key)

                # Log a warning on the console if the reply could not be delivered
                if not send_message(token, room_id, reply):
                    print("Warning: failed to send reply to Webex")

                if should_quit:
                    break

        # Always wait between polls to avoid flooding the Webex API
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

    # Make sure the response is a dictionary before reading from it
    if not isinstance(data, dict):
        return None

    # split() on an empty or missing name gives an empty list, so check it first
    words = str(data.get("displayName", "")).split(maxsplit=1)
    return words[0].lower() if words else None


# Only run the bot when this file is executed directly, not when it is imported
if __name__ == '__main__':
    main()