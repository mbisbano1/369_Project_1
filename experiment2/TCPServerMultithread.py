import socket
import threading

serverPort=11111
serverHost="locahost"
encoding="UTF-8"

running=True

class TCPServerMultithread:
	def __init__(self):
		print("Using server port of %s" % serverPort)

		try:
			serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
			host=socket.gethostname()
			print("Server is running on %s host" % socket.gethostbyname(host))
			serverSocket.bind((host, serverPort))
			serverSocket.listen(5)

			while (running):
				c, addr = serverSocket.accept()
				threading.Thread(target=self.talkToClient, args=(c, addr )).start()

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
		print("Accepted a connection from ", address)

		while 1:
			message=socket.recv(1024).decode(encoding)
			print("Received message: %s" % message)

			socket.send(message.upper().encode(encoding))

			if (message == "shutdown"):
				running=False
			if ((message == "quit") or (message == "shutdown")):
				socket.close()
				return




TCPServerMultithread()
