from socket import *
serverName='localhost'
serverPort=12000

class UDPClient:
	def __init__(self):
		try:
			clientSocket=socket(AF_INET, SOCK_DGRAM)
			message=input("Input lowercase sentence: ")
			clientSocket.sendto(message.encode(), (serverName, serverPort))
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
			print(modifiedMessage.decode())
			clientSocket.close()

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			exit(1)

UDPClient()
