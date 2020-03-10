import socket
from geoip import geolite2
import argparse

if __name__ == '__main__':
	#setup commandline arguements
	parser = argparse.ArgumentParser(description="Get IP Geolocation info")
	parser.add_argument('--hostname', action="store", dest="hostname", required=True)

	#Parse arguements
	given_args = parser.parse_args()
	hostname = given_args.hostname
	ip_address = socket.gethostbyname(hostname)
	print("IP Address:{0}".format(ip_address))

	match = geolite2.lookup(ip_address)
	if match is not None:
		print('Country: ', match.country)
		print('Continent: ', match.continent)
		print('Time Zone: ', match.timezone)
