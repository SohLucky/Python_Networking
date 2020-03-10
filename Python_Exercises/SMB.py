import tempfile
from smb.SMBConnection import SMBConnection

SAMBA_USER_ID = "Cyber"
PASSWORD = "Wp@$$N3"
CLIENT_MACHINE_NAME = 'root'
SAMBA_SERVER_NAME = 'CDSPC046'
SERVER_IP = '192.168.42.160'
SERVER_PORT = 445
SERVER_SHARE_NAME = 'share'
SHARED_FILE_PATH = '/text.txt'

if __name__ == "__main__":
	smb_connection = SMBConnection(SAMBA_USER_ID, PASSWORD, CLIENT_MACHINE_NAME, SAMBA_SERVER_NAME, use_ntlm_v2 = True, domain="WORKGROUP", is_direct_tcp=True)
	assert smb_connection.connect(SERVER_IP, SERVER_PORT)
	shares = smb_connection.listShares()
	for share in shares:
		print(share.name)
	files = smb_connection.listPath(SERVER_SHARE_NAME, '/')
	for file in files:
		print file.filename

	file_obj = tempfile.NamedTemporaryFile()
	file_attributes, filesize = smb_connection.retrieveFile(SERVER_SHARE_NAME,
								SHARED_FILE_PATH, file_obj)
	#Retrieved file contents aer inside file_obj
	file_obj.close()
