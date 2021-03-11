from socket import *
import sys

global server_port
#serverPort=12000
if len(sys.argv) <= 1:
	print('Usage: "python3 UDPServer.py server_port"')
	print('server_port = server socket port: #80GX')
	
	print('Using Default values for server_port')
	print('server_port = 12000')
	server_port = 12000
else:
	server_port = int(sys.argv[1])
	print('server_port = ', server_port)


class UDPServer:
	def __init__(self):
		try:
			serverSocket=socket(AF_INET, SOCK_DGRAM)
			serverSocket.bind(('', server_port))
			print("The server is ready to receive.")
			while 1:
				message, clientAddress = serverSocket.recvfrom(2048)
				modifiedMessage=message.decode().upper()
				serverSocket.sendto(modifiedMessage.encode(), clientAddress)

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			exit(1)

UDPServer()
