# Space Bot: Webex's ISS Tracker

 ## Synopsis
 A Webex bot built on Python, Space Bot tracks the International Space Station (ISS) in real time.  
 In a Webex room, users can question the bot by sending messages in the type `/seconds`, where the number indicates how many seconds it will take for the bot to reply with the ISS's current location.  

 The bot incorporates: **ISS Current Location API** to obtain current ISS coordinates; **Webex Messaging API** to read and write messages in Webex rooms; and **Geocoding API (e.g., Mapbox, OpenWeatherMap, or LocationIQ)** to translate latitude and longitude into places that are readable by humans.  

 ## Features: Watches a Webex room for messages that begin with `/` and end with an integer.  
 The ISS location is retrieved after a predetermined amount of seconds.  
 - Uses a geocoding API to translate ISS latitude and longitude to city, state, and nation.  
 Formatted ISS location messages are sent back to the Webex room; timestamps are converted to a date and time that can be read by humans.
### Sample Results
The ISS was passing over Butterfield Trl Imperial, CA, USA on Friday, February 18, 2022, at 14:09:02 (33.4190°, -115.1074°).

Copy code in Terminal
## Setup Instructions
### 1. Prerequisites
- Python 3.x installed
- `requests` library installed:
```bash
pip install request
Set Up the Bot

Launch a text editor and open space_iss.py.

Enter your Geocoding API key and Webex access token in the placeholders:
MY WEBEX_HARDCODED_TOKEN = "ZDNjZGUyY2UtOGI4OS00ZmYwLWI4ZTgtZjA1NDc5ZTU0YjlkODIwZDZhYjAtMmYy_PE93_d68b3fe9-4c07-4dad-8882-3b3fd6afb92d"
MY GEOCODING_API_KEY = "a6a2ef6a1cfda8adbfbb4b4b30b0da1e"
Launch the Bot

 Open your terminal and navigate to the space_iss.py folder: cd path/to/your/folder
Then run the script: python space_iss.py
Observe the instructions:

 Select if you want to utilise the hard-coded token (y/n).

 Choose the Webex room to keep an eye on

 To find the location of the ISS, send /seconds messages in the Webex chat.

Code Organisation

 The primary bot script is space_iss.py.

 Among the functions are:

 The ISS latitude, longitude, and timestamp are retrieved using the get_iss_location() function.

 The function get_geocode(lat, lon) transforms coordinates into a location that can be read by humans.

 Send a message to the Webex room using send_webex_message(room_id, message).

 Program flow and room monitoring are handled by main().

 Handling Errors

 Try/except blocks are used to catch invalid API responses.

 The handling of missing JSON fields is done with grace. obtain()

 The bot is not crashed by invalid room names or messages.

 Features that are optional

 Integration with SpaceX API to display next launch information

 Recording bot activity for troubleshooting

 Config file support for tokens and API keys instead of hardcoding

 References

 Webex API Documentation

 ISS Current Location API

 Mapbox Geocoding API

 Python time library documentation

Mohammad Abdurahim.
