# Spacebot
The Space Bot monitors a Webex room for messages that begin with / followed by a number (e.g., /5) by integrating Webex Messaging, ISS Current Location, and Geocoding APIs.
After waiting so many seconds, the bot asks the location of the ISS, transforms coordinates into a readable geographic location, and then posts the outcome back to the room.
A. Webex Messaging API
Field	Detail
Base URL	https://webexapis.com/v1
Authentication	Bearer Token
Scopes	spark:rooms_read, spark:messages_read, spark:messages_write
Key Endpoints	GET /rooms, GET /messages?roomId=<id>, POST /messages
Docs	https://developer.webex.com/docs/api/v1/
{
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTIzNDU2Nzg",
  "text": "Hello from Space Bot!"
}
B. ISS Current Location API
Field	Detail
Base URL	http://api.open-notify.org/iss-now.json
Authentication	None
Docs	http://api.open-notify.org/
{
  "timestamp": 1669999999,
  "iss_position": {"latitude": "45.1234", "longitude": "-93.5678"},
  "message": "success"
}
C. Geocoding API (OpenWeatherMap example)
Field	Detail
Base URL	https://api.openweathermap.org/geo/1.0/reverse
Authentication	API Key (appid=YOUR_KEY)
Docs	https://openweathermap.org/api/geocoding-api
Example request:
https://api.openweathermap.org/geo/1.0/reverse?lat=45.1234&lon=-93.5678&limit=1&appid=YOUR_KEY

  
"name": "Minneapolis",
"state": "Minnesota",
"country": "US"

D. The Python Time Library

 used to convert epoch timestamps and handle delays.

 import time
timestamp = 1669999999
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)))

2. MVC and Web Architecture
Component	Responsibility
Model	Interacts with external APIs (Webex, ISS, Geocoding)
View	Webex messages displayed to the user
Controller	Logic interpreting /seconds commands, coordinating API calls

Architecture: Client-Server

Client = Webex user

Server = Python bot (REST client)

