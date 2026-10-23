# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, **Weather API** and a **Geocoding API** , plus the Python time module. Also furhter investigate the application of Web Architecture and MVC design pattern in development of the Bot

---

##  Webex Messaging API (4 marks)

| Criteria                              | HTTP Method | Endpoint / Details                        | Description                                         |
|---------------------------------------|-------------|-------------------------------------------|-----------------------------------------------------|
| API Base URL                          | —           | `https://webexapis.com/v1/`               | Base URL for the Webex REST API                     |
| Authentication Method                 | —           | Bearer Token                              | Authenticates requests using an access token        |
| Endpoint to list rooms                | GET         | `/rooms`                                  | Retrieves a list of rooms                           |
| Endpoint to get messages              | GET         | `/messages?roomId=ROOM_ID`                | Retrieves messages from a specific room             |
| Endpoint to send a message            | POST        | `/messages`                               | Sends a message to a specified room                 |
| Required Headers                      | —           | `Authorization: Bearer YOUR_ACCESS_TOKEN` | Authenticates the API request                       |
| Sample full GET request               | GET         | `https://webexapis.com/v1/rooms`          | Retrieves rooms available to the authenticated user |


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

##  Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria                         | Details                           |
|----------------------------------|-----------------------------------|
| Library used                     | `_______________________________` |
| Function used to convert epoch   | `_______________________________` |
| Sample code to convert timestamp |  
```  
```
|
| Output (human-readable time) | `_______________________________` |

---

##  Extended Feature API ( 3 marks)

| Criteria                                 | Details                           |
|------------------------------------------|-----------------------------------|
| API Provider                             | '_________'                       |
| API Base URL                             | `_______________________________` |
| Endpoint                                 | `_______________________________` |
| Authentication method                    | `_______________________________` |
| Required query parameters                | `_______________________________` |
| Sample JSON response (formatted example) |  
```

```
|

--- 

##  Evaluation – Web Architecture, MVC Design & Security 

In this section, evaluate how web technologies, architecture, and design patterns have been applied in your **AstroBot**. Your responses must relate directly to your implementation and include reflection on your design decisions.

---

###  Web Architecture – Client–Server Model (3 marks)

Explain how the client–server model applies to your AstroBot:

- Identify the **client** 
- Identify the **server(s)** 
- Describe how data flows between:
  - User, AstroBot and APIs

Include a **simple block diagram** to illustrate this interaction.

####  Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate limiting, and Input validation (e.g., handling user commands safely), include examples from code where necessary to illustrate.

---

###  RESTful API Usage in Your Application (3 marks )

Explain how REST APIs are used in your AstroBot: 

- Describe how HTTP methods (GET, POST) are used  
- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)  
- Describe how JSON responses are received and processed  

Note: Relate your explanation directly to your code for higher grade. 

#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses, Avoiding excessive API calls

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
