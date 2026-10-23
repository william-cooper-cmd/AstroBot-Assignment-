# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, **Weather API** and a **Geocoding API** , plus the Python time module. Also, further investigate the application of Web Architecture and MVC design pattern in development of the Bot

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
| Output (human-readable time)     | `strftime("%d/%m/%Y %H:%M:%S %Z")`  |

---

##  Extended Feature API ( 3 marks)

| Criteria                                 | Details                              |
|------------------------------------------|--------------------------------------|
| API Provider                             | The Space Devs, **Launch Library 2** |
| API Base URL                             | `https://ll.thespacedevs.com/2.3.0/` |
| Endpoint                                 | `launches/upcoming`                  |
| Authentication method                    | `None`                               |
| Required query parameters                | `None`                               |
| Sample JSON response (formatted example) | See Below                            |

### Sample JSON Response
 
```json
{
    "count": 476,
    "next": "https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": "7766f3bb-674c-4c71-b986-963bd633fcfe",
            "url": "https://ll.thespacedevs.com/2.3.0/launches/7766f3bb-674c-4c71-b986-963bd633fcfe/",
            "name": "Electron | We're Not Hawking Around (3x HawkEye 360)",
            "response_mode": "normal",
            "slug": "electron-were-not-hawking-around-3x-hawkeye-360",
            "launch_designator": null,
            "status": {
                "id": 3,
                "name": "Launch Successful",
                "abbrev": "Success",
                "description": "The launch vehicle successfully inserted its payload(s) into the target orbit(s)."
            },
            "last_updated": "2026-10-23T11:32:38Z",
            "net": "2026-10-23T07:11:00Z",
            "net_precision": {
                "id": 1,
                "name": "Minute",
                "abbrev": "MIN",
                "description": "The T-0 is accurate to the minute."
            },
            "window_end": "2026-10-23T08:45:00Z",
            "window_start": "2026-10-23T07:00:00Z",
            "image": {
                "id": 1727,
                "name": "[AUTO] Electron - image",
                "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/electron_image_20190705175640.jpeg",
                "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305193613.jpeg",
                "credit": null,
                "license": {
                    "id": 1,
                    "name": "Unknown",
                    "priority": 9,
                    "link": null
                },
                "single_use": true,
                "variants": []
            },
            "infographic": null,
            "probability": 90,
            "weather_concerns": null,
            "failreason": "",
            "hashtag": null,
            "launch_service_provider": {
                "response_mode": "list",
                "id": 147,
                "url": "https://ll.thespacedevs.com/2.3.0/agencies/147/",
                "name": "Rocket Lab",
                "abbrev": "RL",
                "type": {
                    "id": 3,
                    "name": "Commercial"
                }
            },
            "rocket": {
                "id": 7567,
                "configuration": {
                    "response_mode": "list",
                    "id": 26,
                    "url": "https://ll.thespacedevs.com/2.3.0/launcher_configurations/26/",
                    "name": "Electron",
                    "families": [],
                    "full_name": "Electron",
                    "variant": ""
                }
            },
            "mission": {
                "id": 6792,
                "name": "We're Not Hawking Around (3x HawkEye 360)",
                "type": "Earth Science",
                "description": "HawkEye 360 is a a space-based civil global intelligence satellite network using radio frequency (RF) technology to help monitor transportation across air, land and sea and assist with emergencies, and to provide civil SIGINT (Signal Intelligence) mission.\r\n\r\nThe constellation of small satellites (named Hawk ) will collect information on specific radio signals worldwide to provide high-precision radio frequency mapping and analytics from Low Earth orbit (LEO).",
                "image": null,
                "orbit": {
                    "id": 17,
                    "name": "Sun-Synchronous Orbit",
                    "abbrev": "SSO",
                    "celestial_body": {
                        "response_mode": "list",
                        "id": 1,
                        "name": "Earth"
                    }
                },
                "agencies": [
                    {
                        "response_mode": "normal",
                        "id": 1061,
                        "url": "https://ll.thespacedevs.com/2.3.0/agencies/1061/",
                        "name": "HawkEye 360",
                        "abbrev": "he360",
                        "type": {
                            "id": 5,
                            "name": "Private"
                        },
                        "featured": false,
                        "country": [
                            {
                                "id": 2,
                                "name": "United States of America",
                                "alpha_2_code": "US",
                                "alpha_3_code": "USA",
                                "nationality_name": "American",
                                "nationality_name_composed": "Americano"
                            }
                        ],
                        "description": "HawkEye 360 is an American geospatial analytics company headquartered in Herndon, Virginia. It is a commercial seller of radio frequency signal location data gathered by a satellite constellation.",
                        "administrator": "CEO: John Serafini",
                        "founding_year": 2015,
                        "launchers": "",
                        "spacecraft": "HawkEye 360",
                        "parent": null,
                        "image": null,
                        "logo": {
                            "id": 138,
                            "name": "[AUTO] HawkEye 360 - logo",
                            "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/hawkeye2520360_logo_20230807090248.png",
                            "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305185002.png",
                            "credit": null,
                            "license": {
                                "id": 1,
                                "name": "Unknown",
                                "priority": 9,
                                "link": null
                            },
                            "single_use": true,
                            "variants": []
                        },
                        "social_logo": {
                            "id": 60,
                            "name": "[AUTO] HawkEye 360 - social_logo",
                            "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/hawkeye2520360_nation_20230807090249.jpg",
                            "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305184800.jpeg",
                            "credit": null,
                            "license": {
                                "id": 1,
                                "name": "Unknown",
                                "priority": 9,
                                "link": null
                            },
                            "single_use": true,
                            "variants": []
                        },
                        "total_launch_count": 0,
                        "consecutive_successful_launches": 0,
                        "successful_launches": 0,
                        "failed_launches": 0,
                        "pending_launches": 0,
                        "consecutive_successful_landings": 0,
                        "successful_landings": 0,
                        "failed_landings": 0,
                        "attempted_landings": 0,
                        "successful_landings_spacecraft": 0,
                        "failed_landings_spacecraft": 0,
                        "attempted_landings_spacecraft": 0,
                        "successful_landings_payload": 0,
                        "failed_landings_payload": 0,
                        "attempted_landings_payload": 0,
                        "info_url": "https://www.he360.com/",
                        "wiki_url": "https://en.wikipedia.org/wiki/HawkEye_360",
                        "social_media_links": []
                    }
                ],
                "info_urls": [],
                "vid_urls": []
            },
            "pad": {
                "id": 65,
                "url": "https://ll.thespacedevs.com/2.3.0/pads/65/",
                "active": true,
                "agencies": [
                    {
                        "response_mode": "normal",
                        "id": 147,
                        "url": "https://ll.thespacedevs.com/2.3.0/agencies/147/",
                        "name": "Rocket Lab",
                        "abbrev": "RL",
                        "type": {
                            "id": 3,
                            "name": "Commercial"
                        },
                        "featured": true,
                        "country": [
                            {
                                "id": 2,
                                "name": "United States of America",
                                "alpha_2_code": "US",
                                "alpha_3_code": "USA",
                                "nationality_name": "American",
                                "nationality_name_composed": "Americano"
                            }
                        ],
                        "description": "Rocket Lab is an American aerospace manufacturer with a wholly owned New Zealand subsidiary. The company develops lightweight, cost-effective commercial rocket launch services. The Electron Program was founded on the premise that small payloads such as CubeSats require dedicated small launch vehicles and flexibility not currently offered by traditional rocket systems. Its rocket, the Electron, is a light-weight rocket and is now operating commercially. The company is also producing a variety of spacecrafts and spacecrafts components.",
                        "administrator": "CEO: Peter Beck",
                        "founding_year": 2006,
                        "launchers": "Electron",
                        "spacecraft": "",
                        "parent": null,
                        "image": {
                            "id": 24,
                            "name": "[AUTO] Rocket Lab - image",
                            "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/rocket2520lab2520ltd_image_20190207032456.jpeg",
                            "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305184649.jpeg",
                            "credit": null,
                            "license": {
                                "id": 1,
                                "name": "Unknown",
                                "priority": 9,
                                "link": null
                            },
                            "single_use": true,
                            "variants": []
                        },
                        "logo": {
                            "id": 176,
                            "name": "[AUTO] Rocket Lab - logo",
                            "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/rocket2520lab2520ltd_logo_20220218075411.png",
                            "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305185115.png",
                            "credit": null,
                            "license": {
                                "id": 1,
                                "name": "Unknown",
                                "priority": 9,
                                "link": null
                            },
                            "single_use": true,
                            "variants": []
                        },
                        "social_logo": {
                            "id": 88,
                            "name": "[AUTO] Rocket Lab - social_logo",
                            "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/rocket2520lab2520ltd_nation_20230531050352.jpg",
                            "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305184840.jpeg",
                            "credit": null,
                            "license": {
                                "id": 1,
                                "name": "Unknown",
                                "priority": 9,
                                "link": null
                            },
                            "single_use": true,
                            "variants": []
                        }
                    }
                ],
                "name": "Rocket Lab Launch Complex 1A",
                "image": {
                    "id": 1412,
                    "name": "Electron on LC-1A (Return to Sender)",
                    "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/electron25202_image_20201120015105.jpg",
                    "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/255bauto255d__image_thumbnail_20240305192700.jpeg",
                    "credit": "Rocket Lab",
                    "license": {
                        "id": 7,
                        "name": "Rocket Lab Image Use Policy",
                        "priority": 3,
                        "link": "https://www.rocketlabusa.com/about/gallery/"
                    },
                    "single_use": false,
                    "variants": []
                },
                "description": "",
                "info_url": null,
                "wiki_url": "https://en.wikipedia.org/wiki/Rocket_Lab_Launch_Complex_1",
                "map_url": "https://www.google.com/maps?q=-39.262833,177.864469",
                "latitude": -39.262833,
                "longitude": 177.864469,
                "country": {
                    "id": 51,
                    "name": "New Zealand",
                    "alpha_2_code": "NZ",
                    "alpha_3_code": "NZL",
                    "nationality_name": "Kiwi",
                    "nationality_name_composed": "Kiwi"
                },
                "map_image": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/map_images/pad_65_20200803143549.jpg",
                "total_launch_count": 44,
                "orbital_launch_attempt_count": 44,
                "fastest_turnaround": "P7DT14H29M39S",
                "location": {
                    "response_mode": "normal",
                    "id": 10,
                    "url": "https://ll.thespacedevs.com/2.3.0/locations/10/",
                    "name": "Rocket Lab Launch Complex 1, Mahia Peninsula, New Zealand",
                    "celestial_body": {
                        "response_mode": "normal",
                        "id": 1,
                        "name": "Earth",
                        "type": {
                            "id": 1,
                            "name": "Planet"
                        },
                        "diameter": 12742000,
                        "mass": 5.972168e+24,
                        "gravity": 9.80655,
                        "length_of_day": "1 00:00:00",
                        "atmosphere": true,
                        "image": {
                            "id": 2040,
                            "name": "Earth (Apollo 17)",
                            "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/earth_2528apol_image_20240402194304.jpeg",
                            "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/earth_2528apol_image_thumbnail_20240402194305.jpeg",
                            "credit": "NASA",
                            "license": {
                                "id": 4,
                                "name": "NASA Image and Media Guidelines",
                                "priority": 0,
                                "link": "https://www.nasa.gov/nasa-brand-center/images-and-media/"
                            },
                            "single_use": true,
                            "variants": []
                        },
                        "description": "Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
                        "wiki_url": "https://en.wikipedia.org/wiki/Earth",
                        "total_attempted_launches": 7643,
                        "successful_launches": 7086,
                        "failed_launches": 557,
                        "total_attempted_landings": 1381,
                        "successful_landings": 1332,
                        "failed_landings": 49
                    },
                    "active": true,
                    "country": {
                        "id": 51,
                        "name": "New Zealand",
                        "alpha_2_code": "NZ",
                        "alpha_3_code": "NZL",
                        "nationality_name": "Kiwi",
                        "nationality_name_composed": "Kiwi"
                    },
                    "description": "Rocket Lab Launch Complex 1 is a commercial spaceport located close to Ahuriri Point at the southern tip of Māhia Peninsula, on the east coast of New Zealand's North Island. It is owned and operated by private spaceflight company Rocket Lab and supports launches of the company's Electron rocket for small satellites. With the launch of Electron on 25 May 2017, it became the first private spaceport to host an orbital launch attempt, and the first site in New Zealand to host an orbital launch attempt. With the Electron launch of 21 January 2018, it became the first private spaceport to host a successful orbital launch.",
                    "image": {
                        "id": 2206,
                        "name": "Rocket Lab Launch Complex 1",
                        "image_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/rocket_lab_laun_image_20240918164228.jpg",
                        "thumbnail_url": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/images/rocket_lab_laun_image_thumbnail_20240918164228.jpeg",
                        "credit": "Rocket Lab",
                        "license": {
                            "id": 7,
                            "name": "Rocket Lab Image Use Policy",
                            "priority": 3,
                            "link": "https://www.rocketlabusa.com/about/gallery/"
                        },
                        "single_use": true,
                        "variants": []
                    },
                    "map_image": "https://thespacedevs-prod.nyc3.digitaloceanspaces.com/media/map_images/location_10_20200803142509.jpg",
                    "longitude": 177.86586,
                    "latitude": -39.26085,
                    "timezone_name": "Pacific/Auckland",
                    "total_launch_count": 85,
                    "total_landing_count": 17
                }
            },
            "webcast_live": false,
            "program": [],
            "orbital_launch_attempt_count": 7420,
            "location_launch_attempt_count": 85,
            "pad_launch_attempt_count": 44,
            "agency_launch_attempt_count": 98,
            "orbital_launch_attempt_count_year": 247,
            "location_launch_attempt_count_year": 16,
            "pad_launch_attempt_count_year": 9,
            "agency_launch_attempt_count_year": 19
        }
    ]
}
```

--- 

##  Evaluation – Web Architecture, MVC Design & Security 

###  Web Architecture – Client–Server Model (3 marks)

**Client:** AstroBot is a program that acts as an HTTP client. It sends request using the `requests` library. The user interacts through the Webex app, which is also a client of the Webex server.

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

**Secure handling of API keys and tokens:** Credentials are not written into the code. They are loaded from a `.env` file with `python-dotenv` or entered manually at startup, so they can stay out of the repo. The `.env` file is listed in the `.gtignore` so it is never commited to GitHub. The bot also stops if credentials are missing, rather than sending requests that would fail with a 401.

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
- The bot only calls the weather, ISS and launch APIs when a valid command is received not on every poll
- `/launch` is cached for 10 minutes, because the launch Library 2 allows only 15 requests per hour. If a later request fails, the bot falls back to the cached text

```python
LAUNCH_CACHE_SECONDS = 600
if LAUNCH_CACHE["text"] and now - LAUNCH_CACHE["time"] < LAUNCH_CACHE_SECONDS:
    return LAUNCH_CACHE["text"]
```

**Input validation**

- The bot only reacts to messages that @ it followed by `/`. Anything else is ignored.
- Text is normalised with `.lower().strip()` and splits with `partition(" ") into a command and an argument
- The command is compared against a fixed list (`/help`, `/weather`, `/iss`, `/launch`, `/quit`) using `if/elif`. Unknown inputs produce and "Unknown command" message
- An empty argument for `/weather` returns a usage message instead of calling the API
- The city name is passed through the `params` dictionary of `requests`, which URL-encodes it, so user text cannot alter the structure of the request URL

```python
command = message_text[len(bot_name):].strip()
cmd, _, arg = command.partition(" ")
if cmd == "/weather" and not arg:
    send_message(token, room_id, f"Usage @{bot_name} /weather <city>")
```

---

###  RESTful API Usage in Your Application (3 marks )

**HTTP methods** Astro bot uses `GET` to read data and `POST` to create data. All requests are stateless: each one carries its own credentials and the server keeps no session for the bot

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

**How the bot interacts with the APIs** The `/weather` commands a chain of two calls. The bot first sends the city name to the geocoding endpoint to get the coordinates. It then sends them to the weather endpoint. The `/iss` command chains three calls: open-notify gives the ISS position, reverse geocoding turns it into a place name, the weather endpoint gives weather conditions at that place. Replies are sent with a `POST` that contains a JSON body

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

#### Security Considerations: (2 marks)

- **Checking status codes:** each request calls `response.raise_for_status()` inside a `try/except request.RequestExecption` so 4xx and 5xx errors are caught instead of being parsed as valid data
- **Handling invalid or unexpected responses** a failed request returns `None`, an empty list or a clear message, never a crash. Empty results are checked (`if not data`, `if not location`) and `.get()` with default values is used so a missing field such as `visibility` over the ocean does not raise a `KeyError`
- **Avoiding excessive API calls` every request has a `timeout=10` so it cannot hang the bot, the loop sleeps 5 seconds between polls and `/launch` results are cached for 10 minutes

```python
try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
except requests.RequestException:
    return None
```

---

###  MVC Design Pattern in AstroBot (3 Marks)

| Component      | Description and Example (Relate to your Bot)                                                                                                                                                                                                                                                                                                                                                   |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Model**      | The model fetches and holds the data, and has no knowledge of how it is displayed. It contains the functions that call the APIs and return the data: `get_rooms()`, `get_city_coordinates()`, `reverse_geocode()`, `get_weather_by_coords()`, `get_iss_location()` and `get_upcoming_launches()`. Example: `get_city_coordinates("london", key)` returns the geocoding result as a dictionary. |
| **View**       | The view decides how data is presented to the user. `format_weather()` and `format_launch()` turn raw JSON values into readable text, `print_rooms()` shows the room list in the console, and `send_message()` delivers the output to Webex. Example: `format_weather()` produces `Current weather in London, GB: 12°C, light rain \| humidity: 80%... Not good for stargazing`.               |
| **Controller** | The controller receives user input and decides which model and view to use. `main()` polls for the latest message, parses it with `partition(" ")`, and routes it with `if/elif` to the correct function. Example: when the command is `/launch`, the controller calls `get_upcoming_launches()` and passes the result to `send_message()`.                                                    |


---

### 📝 Reflection and Evaluation ( 8 marks )

AstroBot meets the club's core needs. A member can ask for the weather in any city, see where the ISS is with the weather beneath it, and check upcoming launches, all inside the Webex space they already use. The stargazing check is a simple, but it turns rawdata into an answer a member can act on. The extended `/launch` command gives member something to look forward to.

Splitting the code into small functions worked well. Each API has its own fetch function and formating is kept apart, so I could fix and test one section without breaking the others. Adding `/launch` took one function, one `elif` branch and one help line,m  which shows the structure is easy to extend.

The main security risks were exposed credentials, rate limits. Keys live in a `.env` file excluded from Git, request use timeout and status checks, results are cached and commands are matched against a fixed list so unknown input only produces an unknown command message.

Getting the latest message could use a Webex webhook instead of polling, which avoids missed messages when two commands arrive within five seconds. I would split the code into separate model, view and controller modules, add unit tests with mocked API responses.

---

###  Total: /40
