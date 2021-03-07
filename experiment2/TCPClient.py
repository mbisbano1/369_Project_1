import socket
import sys
encoding="UTF-8"

class TCPClient:
	def __init__(self):
		if (len(sys.argv) != 3):
			print("Usage: python3 TCPClient.py server_address server_port")
			exit(1)

		serverAddress=sys.argv[1]
		try:
			serverPort=int(sys.argv[2])
		except ValueError:
			print("Error: input argument invalid.")
			exit(1)

		if ((serverPort <= 1024) or (serverPort >= 65536)):
			print("Error: Server port value must be greater than 1024 and less than 65536.")
			exit(1)

		self.connect(serverAddress, serverPort)


	def connect(self, serverAddress, serverPort):
		try:
			clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				clientSocket.connect((serverAddress, serverPort))
			except ConnectionRefusedError:
				print("Error: Connection refused.")
				exit(1)
				
			print("Type \"quit\" to exit the client, or \"shutdown\" to turn off server.")

			while 1:
				message=input("Enter a message: ")
				clientSocket.send(message.encode(encoding))
				modifiedMessage=clientSocket.recv(1024)
				print("Received message: %s" % modifiedMessage.decode(encoding))

				if ((message == "quit") or (message == "shutdown")):
					break
			
			clientSocket.close()

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			if (clientSocket):
				clientSocket.close()
				print("Socket closed successfully.")

		except Exception as ex:
			print("Exception: %s" % ex)
			if (clientSocket):
				clientSocket.close()
				print("Socket closed successfully.")

TCPClient()
