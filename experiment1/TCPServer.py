from socket import *
serverPort=12000

class TCPServer:
	def __init__(self):
		try:
			serverSocket=socket(AF_INET, SOCK_STREAM)
			serverSocket.bind(('', serverPort))
			serverSocket.listen(1)
			print("The server is ready to receive.")
			while 1:
					connectionSocket, addr = serverSocket.accept()
					sentence=connectionSocket.recv(1024).decode()
					capitalizedSentence=sentence.upper()
					connectionSocket.send(capitalizedSentence.encode())
					connectionSocket.close()

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			exit(1)

TCPServer()
