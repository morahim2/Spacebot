... WEBEX_HARDCODED_TOKEN = "ZDNjZGUyY2UtOGI4OS00ZmYwLWI4ZTgtZjA1NDc5ZTU0YjlkODIwZDZhYjAtMmYy_PE93_d68b3fe9-4c07-4dad-8882-3b3fd6afb92d"
... GEOCODING_API_KEY = "a6a2ef6a1cfda8adbfbb4b4b30b0da1e"  
... 
... 
... 
... def get_webex_headers(token):
...     """Return Webex API headers."""
...     return {"Authorization": f"Bearer {token}"}
... 
... def list_webex_rooms(headers):
...     """Return a list of Webex rooms."""
...     url = "https://webexapis.com/v1/rooms"
...     response = requests.get(url, headers=headers)
...     response.raise_for_status()
...     rooms = response.json()["items"]
...     print("\nList of rooms:")
...     for room in rooms:
...         print(f"Type: {room['type']}, Name: {room['title']}")
...     return rooms
... 
... def find_room_id(rooms, room_name):
...     """Find the room ID by name."""
...     for room in rooms:
...         if room_name.lower() in room['title'].lower():
...             print(f"Found room: {room['title']}")
...             return room['id']
...     return None
... 
... def get_latest_message(room_id, headers):
    """Return the latest message text in a room."""
    url = f"https://webexapis.com/v1/messages?roomId={room_id}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    messages = response.json()["items"]
    if messages:
        return messages[-1]['text']
    return None

def get_iss_location():
    """Return current ISS latitude, longitude, and timestamp."""
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']
    timestamp = datetime.fromtimestamp(int(data['timestamp']))
    return lat, lon, timestamp

def get_geocode(lat, lon, api_key):
    """Return city, state, country from coordinates using Geocoding API."""
    url = f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    location_info = response.json()
    if location_info:
        info = location_info[0]
        city = info.get('name', '')
        state = info.get('state', '')
        country = info.get('country', '')
        return city, state, country
    return '', '', ''

def send_webex_message(room_id, headers, message):
    """Send a message to the specified Webex room."""
    url = "https://webexapis.com/v1/messages"
    data = {"roomId": room_id, "text": message}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()


def main():
    
    use_token = input("Do you wish to use the hard-coded Webex token? (y/n) ")
    if use_token.lower() != 'y':
        access_token = input("Enter your Webex access token: ")
    else:
        access_token = WEBEX_HARDCODED_TOKEN

    headers = get_webex_headers(access_token)


    rooms = list_webex_rooms(headers)


    room_name = input("\nWhich room should be monitored for /seconds messages? ")
    room_id = find_room_id(rooms, room_name)
    if not room_id:
        print("Room not found. Exiting...")
        return

    print("\nMonitoring room for messages starting with '/<seconds>'...")

    last_message = None

    while True:
        try:
            message = get_latest_message(room_id, headers)
            if message and message != last_message:
                print("Received message:", message)
                last_message = message

                if message.startswith("/"):
                    try:
                        delay_seconds = int(message[1:])
                        print(f"Waiting {delay_seconds} seconds before checking ISS location...")
                        time.sleep(delay_seconds)

                       
                        lat, lon, timestamp = get_iss_location()

                      
                        city, state, country = get_geocode(lat, lon, GEOCODING_API_KEY)

                       
                        response_message = (
                            f"On {timestamp}, the ISS was flying over "
                            f"{city}, {state}, {country} ({lat}°, {lon}°)"
                        )

                        
                        send_webex_message(room_id, headers, response_message)
                        print("Sent message to Webex:", response_message)
                    except ValueError:
                        print("Invalid format: please use /<number_of_seconds>")
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nExiting program...")
            break
        except Exception as e:
            print("Error:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()
