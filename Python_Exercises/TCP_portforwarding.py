import sshtunnel
from getpass import getpass

ssh_host = "localhost"
ssh_port = 22
ssh_user = "root"

REMOTE_HOST = "192.168.154.145"
REMOTE_PORT = 21

from sshtunnel import SSHTunnelForwarder
ssh_pass = getpass("Enter your ssh password: ")

server = SSHTunnelForwarder(ssh_address=(ssh_host,ssh_port), 
			ssh_username=ssh_user, ssh_password=ssh_pass,
			remote_bind_address=(REMOTE_HOST, REMOTE_PORT))

server.start()
print("Connect the remote service vai loca port: %s" %server.local_bind_port)
#work with FTP service via the server.local_bind_port

try:
	while True:
		pass
except KeyboardInterrupt:
	print("Exiting user request.\n")
	server.stop()
