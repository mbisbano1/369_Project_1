import socket
import sys, threading, time
import queue

# constant definitions
maxNumPeers = 10
TimeoutDelay = 5
masterPort = 42069
serverPort = 12000
clientPortStartingNum = 12001
peerFlag = 'ECE369 TCPP2P ACTIVE '


class TCPpeer:
	"""TCP P2P Class/Object"""
	hostname = ''			# Each peer has it's own hostname
	addr = ''               # Each peer has it's own address
	peersList = []          # Each peer maintains a list of other peers addresses.add()
	peersConnectedList = [] # each peer has a flag for if a client is connected to it.
	serverRunning = False	# Each peer has a status for it's server and client side
	clientRunning = False	# ...
	numClients = 0

	isMaster = False
	isNextMaster = False
	masterTimeOut = False 

	newPeersList = False


	wantToShutdown = False
	readyToShutdown = False
	peerRunning = False	

	#peerScanRunning = False # Each peer has a status for if it is still accepting UDP broadcast messages to map other peers in network


	def Master(self):	# The master maintains the peersList and checks for peers that have timed out
		try:
			MasterS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			MasterS.bind(('', masterPort))
			while(self.isMaster):
				try:
					message, clientAddress = MasterS.recvfrom(2048)
					rxPeerFlag = message.decode()[0:21]
					
					if ((rxPeerFlag == peerFlag) and (clientAddress[0] not in self.peersList)):
						# update peersList, set newPeersList flag
						self.peersList.append(clientAddress[0])
						print("Appended ", clientAddress[0], " to peersList")
						self.newPeersList = True

						# delay a tiny bit (200mS)
						time.sleep(0.2)

						# send peersList to new peer! Welcome to the fun!
						peersListStr = ' '.join(self.peersList)
						MasterS.sendto(peersListStr.encode(), clientAddress)
					else:
						print("Sorry")
						print(rxPeerFlag + 'rx')
						print(peerFlag + 'df')


				except Exception as ex:
					print("Master While Exception: %s" %ex)
					sys.exit(1)


		except KeyboardInterrupt:
				print("Keyboard Interrupt!")
				exit(1)
		except Exception as ex:
			print("Master Exception: %s" % ex)
			sys.exit(1)


	def nextMaster(self):	# does stuff to prepare to carry the torch
		a = 0

	def broadcastHandler(self):
		try:	# Try sending broadcast to scan for other peers on network
			BroadcastS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			BroadcastS.settimeout(TimeoutDelay)
			broadcastMessage = peerFlag + self.addr
			#BroadcastS.sendto(broadcastMessage,('255.255.255.255', 12000))
			BroadcastS.sendto(broadcastMessage.encode(),('<broadcast>', 12000))
			print("Broadcast Sent!")
			print("Wait", str(TimeoutDelay) ,"seconds for response:")
			#self.peerScanRunning = True
			#while self.peerScanRunning:
			try:
				peerListMessage, masterAddressTuple = BroadcastS.recvfrom(2048)
				self.masterIPAddress = masterAddressTuple[0]
				self.masterPort = masterAddressTuple[1]

				# split message and store peers in peersList.
				self.peersList.append(peerListMessage.decode().split(" "))
				self.isMaster = False
				if len(self.peersList) != 1:
					print("Closing the Broadcast Socket")
					BroadcastS.close		
					sys.exit(0)
				else:
					self.isNextMaster = True
					print("You are the next Master! Be prepared!")
					

			except KeyboardInterrupt:
				print("Keyboard Interrupt!")
				exit(1)
			except socket.timeout:		# will timeout in 10 seconds!
				print("You are the Master on this Network! Congrats!")
				self.isMaster = True
				self.peersList.append(self.addr)	#append master address to first slot in peersList
				#start master thread!
				#master_thread = threading.Thread(target=self.Master, args=())
				#master_thread.start()
				#print("Master Thread Started!")
			except Exception as ex:		
				print("Broadcast Handler Internal Exception: %s" % ex)
				sys.exit(1)				



			
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Broadcast Handler Exception: %s" % ex)
			exit(1)
		# do something, not implemented yet

	def clientTask(self, targetServerAddr, targetServerPort):
		try:
			clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			try:
				clientSocket.connect((targetServerAddr, targetServerPort))
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


	def clientSideManager(self):
		try:
			masterAddr = self.peersList[0]
			masterClient_thread = threading.Thread(target=self.clientTask, args=(self, masterAddr, serverPort))
			masterClient_thread.start()
			self.numClients = self.numClients + 1
			self.peersConnectedList.append(True)
		except Exception as ex:
			print("clientSideManager MasterClient Exception: %s" %ex)
			sys.exit(1)

		while(self.peerRunning):
			if(self.newPeersList):
				correctNumClients = len(self.peersList)-1
				self.indexInPeersList = self.peersList.index(self.addr); 
				#startIndex = self.numClients
				
				for i in range(1, len(self.peersList)):
					if (i != self.indexInPeersList) and ( = len(self.peersConnectedList)):
						 self.peersConnectedList.append(True)
						#hi = 2

				self.newPeersList = False

		#clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def serverSide(self):
		try:
			serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			serverSocket.bind(('', serverPort))
			serverSocket.listen(maxNumPeers)
			print("The server is ready to receive" + str(maxNumPeers) +"peers.")
			while 1:
					connectionSocket, addr = serverSocket.accept()
					sentence=connectionSocket.recv(1024).decode()
					capitalizedSentence=sentence.upper()
					connectionSocket.send(capitalizedSentence.encode())
					connectionSocket.close()

		except KeyboardInterrupt:
			print("Keyboard interrupt")
			exit(1)
		except Exception as ex:
			print("Server Exception: %s" %ex)

	def __init__(self):
		self.hostname = socket.gethostname()
		self.addr = socket.gethostbyname(self.hostname)
		print("Hostname is: ", self.hostname)
		print("IP address is: ", self.addr)
		#self.serverRunning = True
		
		broadcastHandler_thread = threading.Thread(target=self.broadcastHandler, args=())
		broadcastHandler_thread.start()
		print("Started the Broadcast Handler Thread, it will scan for other peers to connect to!")

		# wait for broadcastHandler thread to determine role
		time.sleep(TimeoutDelay + 3)

		if self.isMaster:	
			master_thread = threading.Thread(target=self.Master, args=())
			master_thread.start()
			print("Master Thread Started!")
		if self.isNextMaster:
			nextMaster_thread = threading.Thread(target=self.nextMaster, args=())
			nextMaster_thread.start()
			print("Next Master thread started!")
		
		self.peerRunning = True

		server_thread = threading.Thread(target=self.serverSide, args=())
		server_thread.start()
		print("Started the Server thread")

		client_thread = threading.Thread(target=self.clientSideManager, args=())
		client_thread.start()
		print("Started the Client thread")
		




TCPpeer()