from socket import *
serverPort=12000

class UDPServer:
	def __init__(self):
		try:
			serverSocket=socket(AF_INET, SOCK_DGRAM)
			serverSocket.bind(('', serverPort))
			print("The server is ready to receive.")
			while 1:
				message, clientAddress = serverSocket.recvfrom(2048)
				modifiedMessage=message.decode().upper()
				serverSocket.sendto(modifiedMessage.encode(), clientAddress)

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			exit(1)

UDPServer()
