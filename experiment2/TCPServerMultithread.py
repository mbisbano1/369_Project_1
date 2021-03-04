import socket
import threading

serverPort=11111
serverHost="locahost"

class TCPServerMultithread:
	def __init__(self):
		print("Using server port of %s" % serverPort)
		running=True

		try:
			serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
			host=socket.gethostname()
			print("Server is running on %s host" % socket.gethostbyname(host))
			serverSocket.bind((host, serverPort))
			serverSocket.listen(5)

			while (running):
				print("Threaded TCP server listening on port %s" % serverPort)
				threading.Thread(target=self.talkToClient, args=(serverSocket.accept()))

			print("Server shutting down")
			serverSocket.shutdown(0)
			serverSocket.close()

		except IOError:
			if (serverSocket):
				serverSocket.close()
			print("Error opening socket.")
			exit(1)

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			if (serverSocket):
				serverSocket.close()
				print("Socket closed successfully.")
			exit(1)


	def talkToClient(connectionSocket, socket, address):
		print("Accepted a connection from %s" % address)

		while 1:
			message=connectionSocket.recv(1024)
			print("Received message: %s" % message)

			connectionSocket.send(message.upper())

			if (message == "shutdown"):
				running=0
			elif ((message == "quit") or (message == "shutdown")):
				connectionSocket.close()
				break

TCPServerMultithread()
