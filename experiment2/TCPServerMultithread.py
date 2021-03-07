import socket
import threading
import traceback
import sys

encoding="UTF-8"
running=True

class TCPServerMultithread:
	def __init__(self):
		if (len(sys.argv) != 2):
			print("Usage: python3 TCPServerMultithread.py server_port")
			exit(1)

		try:
			serverPort=int(sys.argv[1])
		except ValueError:
			print("Error: input argument invalid.")
			exit(1)

		if ((serverPort <= 1024) or (serverPort >= 65536)):
			print("Error: Server port value must be greater than 1024 and less than 65536.")
			exit(1)


		print("Using server port %s" % serverPort)

		try:
			serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
			host=socket.gethostname()
			serverSocket.bind((host, serverPort))
			serverSocket.listen(5)

			threadList=[]

			while (running):
				c, addr = serverSocket.accept()
				temp=threading.Thread(target=self.talkToClient, args=(c, addr ))
				temp.daemon=True
				temp.start() 
				threadList.append(temp)

			for thread in threadList:
				thread.join()

			serverSocket.shutdown(0)
			serverSocket.close()

		except IOError:
			if (serverSocket):
				serverSocket.close()
			print("Error: Could not open socket.")
			exit(1)

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			if (serverSocket):
				serverSocket.close()
				print("Socket closed successfully.")
			exit(1)


	def talkToClient(self, socket, address):
		print("Accepted a connection from ", address)
		watchdog=0

		while (watchdog < 50): 
			watchdog+=1
			message=socket.recv(1024).decode(encoding)
			print("Received message: %s" % message)

			socket.send(message.upper().encode(encoding))

			if (message == "shutdown"):
				socket.close()
				break
			elif (message == "quit"):
				socket.close()
				break

		running=False

TCPServerMultithread()
