from socket import *

serverName='localhost'
serverPort=12000

class TCPClient:
	def __init__(self):
		try:
			clientSocket=socket(AF_INET, SOCK_STREAM)

			try:
				clientSocket.connect((serverName, serverPort))
			except ConnectionRefusedError:
				print("[Error] Connection refused. Exiting.")
				exit(1)

			sentence=input("Input lowercase sentence: ")
			clientSocket.send(sentence.encode())
			modifiedSentence=clientSocket.recv(1024) #blocking
			print("From server: %s" % modifiedSentence.decode())
			clientSocket.close()

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			exit(1)

TCPClient()
