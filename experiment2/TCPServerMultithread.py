import socket
import threading
import traceback

serverPort=11111
encoding="UTF-8"

running=True

class TCPServerMultithread:
	def __init__(self):
		print("Server port is %s" % serverPort)

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
			print("Error opening socket.")
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
