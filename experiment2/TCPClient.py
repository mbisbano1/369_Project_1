import socket

serverAddress="localhost"
serverPort=11111

class TCPClient:
	def __init__(self):
		clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			clientSocket.connect((serverAddress, serverPort))
		except ConnectionRefusedError:
			print("Error: Connection refused.")
			exit(1)
			

		print("Type \"quit\" to exit the client, or \"shutdown\" to turn off server.")

		while 1:
			message=input("Enter a message: ")
			clientSocket.send(message)
			modifiedMessage=clientSocket.recv(1024)
			print("Received message: %s" % modifiedMessage)

			if ((message == "quit") or (message == "shutdown")):
				print("Client exit")
				break

		clientSocket.close()

TCPClient()
