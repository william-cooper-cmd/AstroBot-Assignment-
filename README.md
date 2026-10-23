# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, **Weather API** and a **Geocoding API** , plus the Python time module. Also furhter investigate the application of Web Architecture and MVC design pattern in development of the Bot

---

##  Webex Messaging API (4 marks)

| Criteria                   | HTTP Method | Endpoint / Details                                                         | Description                                         |
|----------------------------|-------------|----------------------------------------------------------------------------|-----------------------------------------------------|
| API Base URL               | —           | `https://webexapis.com/v1/`                                                | Base URL for the Webex REST API                     |
| Authentication Method      | —           | Bearer Token                                                               | Authenticates requests using an access token        |
| Endpoint to list rooms     | GET         | `/rooms`                                                                   | Retrieves a list of rooms                           |
| Endpoint to get messages   | GET         | `/messages?roomId=ROOM_ID`                                                 | Retrieves messages from a specific room             |
| Endpoint to send a message | POST        | `/messages`                                                                | Sends a message to a specified room                 |
| Required Headers           | —           | `Authorization: Bearer YOUR_ACCESS_TOKEN Content-Type: "application/json"` | Authenticates the API request                       |
| Sample full GET request    | GET         | `https://webexapis.com/v1/rooms`                                           | Retrieves rooms available to the authenticated user |


### Sample JSON Response (List Rooms)

```json
{
    "items": [
      {
            "id": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vY2ExNjU1ZTAtY2Q4Mi0xMWYxLWExMWYtYmI5YWYwOGY5OTlk",
            "title": "William Cooper",
            "type": "direct",
            "lastActivity": "2026-10-21T19:08:59.470Z",
            "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMGRhY2VkNi1iYjdhLTQ4NTEtODRjOS1mYjQyMjhkNTAyNzA",
            "created": "2026-10-21T19:08:24.510Z",
            "ownerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jMThlMTNhZS01NTc1LTRiYzAtYWUwMS1lNDg5MDVmMTRmMTc",
            "isPublic": false,
            "isReadOnly": false,
            "isLocked": false
      }
   ]
}
```

---

##  ISS Current Location API (2 marks)

| Criteria                              | Details                       |
|---------------------------------------|-------------------------------|
| API Base URL                          | `http://api.open-notify.org/` |
| Endpoint for current ISS location     | `GET /iss-now.json`           |
| Sample response format (example JSON) | See below                     |

### Sample JSON Response

```json
{
  "message": "success",
  "timestamp": 1791362217,
  "iss_position": {
    "longitude": "72.3341",
    "latitude": "49.0602"
  }
}
```

---

## Geocoding API (4 marks)

| Criteria                         | Details                                                                                         |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| Provider used (Choose one)       | **OpenWeatherMap**                                                                              |
| API Base URL                     | `https://api.openweathermap.org/`                                                               |
| Endpoint for geocoding           | `geo/1.0/direct`                                                                                |
| Endpoint for reverse geocoding   | `geo/1.0/reverse`                                                                               |
| Authentication method            | `API Key`                                                                                       |
| Required query parameters        | `appid`, `q`, `lat`, `lon`                                                                      |
| Sample forward geocoding request | `https://api.openweathermap.org/geo/1.0/direct?q=Zocca,IT&limit=1&appid=YOUR_API_KEY`           |
| Sample reverse geocoding request | `https://api.openweathermap.org/geo/1.0/reverse?lat=44.34&lon=10.99&limit=1&appid=YOUR_API_KEY` |
| Sample JSON response             | See below                                                                                       |

### Sample JSON Response (Reverse Geocoding)

```json
[
    {
        "name": "Zocca",
        "lat": 44.3472638,
        "lon": 10.990407,
        "country": "IT",
        "state": "Emilia-Romagna"
    }
]
```

---


##  Weather API (3 marks)

| Criteria                               | Details                                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------------------|
| Provider used (Choose one)             | **OpenWeatherMap**                                                                                    |
| API Base URL                           | `https://api.openweathermap.org/`                                                                     |
| Endpoint for current weather           | `data/2.5/weather`                                                                                    |
| Authentication method                  | `API Key`                                                                                             |
| Required query parameters              | `appid`, `lat`, `lon`                                                                                 |
| Sample request with latitude/longitude | `https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=YOUR_API_KEY&units=metric` |
| Sample JSON response                   | See below                                                                                             |

### Sample JSON Response

```json
{
  "coord": {
    "lon": 10.99,
    "lat": 44.34
  },
  "weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "broken clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 14.59,
    "feels_like": 13.83,
    "temp_min": 12.34,
    "temp_max": 14.59,
    "pressure": 1019,
    "humidity": 66,
    "sea_level": 1019,
    "grnd_level": 955
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.48,
    "deg": 254,
    "gust": 6.76
  },
  "clouds": {
    "all": 62
  },
  "dt": 1792754048,
  "sys": {
    "type": 2,
    "id": 2044440,
    "country": "IT",
    "sunrise": 1792734043,
    "sunset": 1792772386
  },
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",
  "cod": 200
}
```


---

##  Epoch to Human Time Conversion (Python datetime module) (2 marks)

| Criteria                         | Details                             |
|----------------------------------|-------------------------------------|
| Library used                     | `datetime`                          |
| Function used to convert epoch   | `.fromtimestamp`                    |
| Sample code to convert timestamp | `datetime.fromtimestamp(timestamp)` |

| Output (human-readable time) | `strftime("%d/%m/%Y %H:%M:%S %Z")` |

---

##  Extended Feature API ( 3 marks)

| Criteria                                 | Details                                 |
|------------------------------------------|-----------------------------------------|
| API Provider                             |  The Space Devs, **Launch Library 2**   |
| API Base URL                             | `https://ll.thespacedevs.com/2.2.0/`    |
| Endpoint                                 | `launch/upcoming/`                      |
| Authentication method                    | `None`                                  |
| Required query parameters                | `None`                                  |
| Sample JSON response (formatted example) | See Below                               |

### Sample JSON Response
 
```json
{
  "count": 120,
  "next": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=3&offset=3",
  "previous": null,
  "results": [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "name": "Falcon 9 Block 5 | Starlink Group 10-1",
      "status": {
        "id": 1,
        "name": "Go for Launch"
      },
      "net": "2026-10-25T14:30:00Z",
      "launch_service_provider": {
        "id": 121,
        "name": "SpaceX"
      },
      "pad": {
        "name": "Space Launch Complex 40",
        "location": {
          "name": "Cape Canaveral SFS, FL, USA"
        }
      }
    }
  ]
}
```

--- 

##  Evaluation – Web Architecture, MVC Design & Security 

###  Web Architecture – Client–Server Model (3 marks)

**Client:** AstroBot is a program that acts as a HTTP client. It sends request using the `requests` library. The user interacts through the Webex app, which is also a client of the Webex server.

| Server                    | Role in the bot                                         |
|---------------------------|---------------------------------------------------------|
| Webex (`webexapis.com`)   | Stores the chat room, delivers and accepts messages     |
| OpenWeatherMap            | Geocoding, reverse geocoding and current weather        |
| Open Notify               | Current ISS position and timestamp                      |
| Launch Library 2          | Upcoming rocket launches (extended feature)             |

**Data Flow:** The bot does not receive messages directly, instead it polls Webex every 5 seconds.

1. The user types a command into the Webex space. e.g. `@Astro /weather London`
2. The Webex server stores the message
3. AstroBot sends `GET /messages` and receives the latest message as a json
4. The controller pareses the command calls the matching function
5. That function sends `GET` requests to the relevant API servers 
6. The bot formats the JSON into readable text and sends `POST /messages` to Webex
7. The Webex server delivers the reply to the user

Include a **simple block diagram** to illustrate this interaction.

####  Security Considerations: (3 marks )

**Secure handling of API keys and tokens:** Credentials are not written into the code. They are loaded from a `.env` file with `python-dotenv` or entered manually at startup, so they can stay out of the repo. The `.env` file is listed in the `.gtignore` so it is never commited to Github. The bot also stops if credentials are missing, rather than sending requests that would fail with a 401.

```python
load_dotenv()
token = os.getenv("WEBEX_TOKEN")
weather_key = os.getenv("API_KEY")
 
if not token or not weather_key:
    print("Missing Webex token or Weather API key")
    return
```
***API rate limiting:*** 

- The polling loops always ends with `time.sleep(5)` so the bot doesn't get rate limited form Webex
- The bot only calls the weather, iSS and launch APIs when a vlaid command is recieved not on evedry poll
- `/launch` is cached for 10 minutes, because the launch Library 2 allows only 15 requests per hour. If a later request fails, the bot falls back to the chached text

```python
LAUNCH_CACHE_SECONDS = 600
if LAUNCH_CACHE["text"] and now - LAUNCH_CACHE["time"] < LAUNCH_CACHE_SECONDS:
    return LAUNCH_CACHE["text"]
```

**Input validation**

- The bot only reacts to messages that @ it followed by `/`. Anything else is ignored.
- Text is normalised with `.lower().strip()` and splits with `partition(" ") into a command and an argument
- The command is compared agaist a fixed list (`/help`, `/weather`, `/iss`, `/launch`, `/quit`) using `if/elif`. Unknown inputs produce and "Unknown command" message
- An empty argument for `/weather` returns a usage message instead of calling the API
- The city name is passed through the `params` dicitionary of `requests`, which URL-encodes it, so user text cannot alter the structure of the request URL

```python
command = message_text[len(bot_name):].strip()
cmd, _, arg = command.partition(" ")
if cmd == "/weather" and not arg:
    send_message(token, room_id, f"Usage @{bot_name} /weather <city>")
```

---

###  RESTful API Usage in Your Application (3 marks )

**HTTP methods** Astro bot uses `GET` to read data and `POST` to create data. All requests are stateless: each one carries its own credetials and the server keeps no session for the bot

| API              | Method | Endpoint                     | Purpose                                    | Function in code                           |
|------------------|--------|------------------------------|--------------------------------------------|--------------------------------------------|
| Webex            | GET    | `/rooms`                     | List the rooms the bot can access          | `get_rooms()`                              |
| Webex            | GET    | `/people/me`                 | Get the bot's display name                 | `main()`                                   |
| Webex            | GET    | `/messages?roomId=...&max=1` | Read the latest message mentioning the bot | `get_latest_message()`                     |
| Webex            | POST   | `/messages`                  | Send a reply to the room                   | `send_message()`                           |
| OpenWeatherMap   | GET    | `/geo/1.0/direct`            | City name to latitude and longitude        | `get_city_coordinates()`                   |
| OpenWeatherMap   | GET    | `/geo/1.0/reverse`           | ISS coordinates to nearest place name      | `reverse_geocode()`                        |
| OpenWeatherMap   | GET    | `/data/2.5/weather`          | Current weather at coordinates             | `get_weather()`, `get_weather_by_coords()` |
| Open Notify      | GET    | `/iss-now.json`              | Current ISS position and timestamp         | `get_iss_location()`                       |
| Launch Library 2 | GET    | `/launch/upcoming/`          | Upcoming rocket launches                   | `get_upcoming_launches()`                  |

**How the bot ineracts with the APIs** The `/weather` cmmandis a chain of two calls. The bot first sends the city name to the gecoding endpoint to get the coordiantes. It then sends them to the weather endpoint. The `/iss` command chains three calls: open-notify gives the ISS position, reverse geocoding turns it into a place name, the weather endpoint gives weather conditions at that place. Replies are sent with a `POST` that contains a JSON body

```python
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
data = {"roomId": room_id, "text": message}
requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
```
**How JSON response are processes** Every API replies with JSON. The bot calls `response.json()` which turns the body into python dictionaries, then extracts only the fields it needs. For example the geocoding response is a list, so the bot takes the first item, and the weather response is a nested dictionary

```python
data = response.json()
return data[0] if data else None          
 
temp = weather.get('main', {}).get('temp', 'N/A')   # weather: nested dict
```

`format_weather()` and `format_launch()` then convert the extracted values into a readable string, including the stargazing verdict, which combines cloud cover, visibility, humidity and wind speed.


---

###  MVC Design Pattern in AstroBot (3 Marks)

Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation

| Component      | Description and Example (Relate to your Bot) |
|----------------|----------------------------------------------|
| **Model**      |                                              |
| **View**       |                                              |
| **Controller** |                                              |

---

### 📝 Reflection and Evaluation ( 8 marks )

Reflect on your AstroBot (400 words):

- How effective is your bot in meeting the Astronomy Club’s needs?  
- What design decisions worked well?  
- What challenges did you face when integrating APIs?  
- What security risks did you identify and how were they handled?  
- How could your solution be improved in the future?  

---

###  Total: /40
