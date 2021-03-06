import socket

serverAddress="127.0.1.1"
serverPort=11111
encoding="UTF-8"

class TCPClient:
	def __init__(self):
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