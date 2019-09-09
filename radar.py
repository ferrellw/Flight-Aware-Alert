import requests
import sys
import time
import playsound
import json

server = sys.argv[1]
flight = str.upper(sys.argv[2])
flight = flight.strip()

def track(flight,server):
	while True:
		response = requests.get(url="http://"+server+"/data/aircraft.json")
		data = json.loads(response.content)
		status_code = ('<{status_code}>'.format(status_code=response.status_code))
		if status_code == "<404>":
			print "Error. Check server address and try again..."
			sys.exit(1)
		for i in data['aircraft']:
			try:
				flight_data = str(i['flight'])
				flight_data = flight_data.strip()
				if flight == flight_data:
					print "Spotted %s at %s : https://www.google.com/maps/search/?api=1&query=%s,%s" % (flight,time.strftime("%I:%M:%S"),i['lat'],i['lon'])
					playsound.playsound('sonar.mp3', True)
			except KeyError:
				continue
		else:
			print "Nothing yet. We'll keep looking for %s" % flight
		time.sleep(5)

track(flight,server)