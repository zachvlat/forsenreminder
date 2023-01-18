import requests

myStreamer = input("type 'forsen' to see if forsen is live: ")

url = "https://gwyo-twitch.p.rapidapi.com/stream/" + myStreamer

headers = {
	"X-RapidAPI-Key": "ff9402c761mshc899600518864e1p1cdb2fjsn523d5efaa070",
	"X-RapidAPI-Host": "gwyo-twitch.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

if response.text == "{}" :
    print ("forsen is ded feelsbadman")
else:
    print("LIVE KKool GuitarTime")
