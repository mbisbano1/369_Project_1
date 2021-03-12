import socket
import sys, threading

class UDPPeer:
	"""UDP P2P Class/Object"""
	hostname = ''			# Each peer has it's own hostname
	addr = ''               # Each peer has it's own address
	peersList = []          # Each peer maintains a list of other peers addresses.add()
	ServerPort = 12000      # Each peer uses port 12000 for now?
	ClientPort = 12001      # Each peer has it's output/client side port at 12001 for now
	serverRunning = True	# Each peer has a status for it's server and client side
	clientRunning = True	# ...
	
	def serverSide(self):
		print("Starting Server Thread!")
		try:	# Try setting up the server
			serverS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			serverS.bind(('',self.ServerPort))
			print("ServerSide is ready to receive.")
			while self.serverRunning:
				message, clientAddress = serverS.recvfrom(2048)
				print("Message Received from: ", clientAddress)
				print(message.decode())
				if (message.decode()[0:20] == ' ECE369 Peer Active ') and (clientAddress not in self.peersList):
					self.peersList.append(clientAddress[0])
					print("Appended ", clientAddress[0], " to peersList")
				elif (clientAddress in self.peersList) and (message.decode()[0:18] == ' ECE369 Peer Quit '):
					self.peersList.remove(clientAddress[0]) 
					print("Removed ", clientAddress[0], " from peersList")
				
				ackMessage = 'Receipt Acknowledged from: ' + self.addr
				serverS.sendto(ackMessage.encode(), (clientAddress[0], self.ServerPort))
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)
	
	def clientSide(self):
		print("Starting Client Thread!")	
		try:
			clientS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			clientS.settimeout(1)	# set socket timeout as 1 second
			typedInput=input("Input message to send: ")
			message = ''
			if typedInput == 'Quit':
				message = ' ECE369 Peer Quit ' + self.addr
			else:
				message = typedInput
			for peer in self.peersList:
				try:	# Try to send message to each peer in peersList
					clientS.sendto(message.encode(), (peer, self.ServerPort))
					responseMessage, peerAddress = clientS.recvfrom(2048)
					print("Acknowledge Received from ", peerAddress)
					print(responseMessage)
				except KeyboardInterrupt:
					print("Keyboard Interrupt!")
					exit(1)
				except TimeoutError as ex:
					print("Timout Exception: %s" % ex)
					self.peersList.remove(peer)
					print("Removed ", peer, " from peersList")
				except Exception as ex:
					print("Exception: %s" % ex)
					exit(1)

		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)

	def __init__(self):
		#self.addr = input("Enter your IP Address from ifconfig: eg. 192.168.0.150")
		self.hostname = socket.gethostname()
		self.addr = socket.gethostbyname(self.hostname)
		print("Hostname is: ", self.hostname)
		print("IP address is: ", self.addr)
		self.serverRunning = True
		try:	# Try sending broadcast to scan for other peers on network
			BroadcastS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			broadcastMessage = ' ECE369 Peer Active ' + self.addr
			#BroadcastS.sendto(broadcastMessage,('255.255.255.255', 12000))
			BroadcastS.sendto(broadcastMessage.encode(),('<broadcast>', 12000))
			BroadcastS.close
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)

		try:	# Try setting up threads for handling the client and server side of this peer
			# Create two new threads
			serverThread = threading.Thread(target=self.serverSide, args=())
			clientThread = threading.Thread(target=self.clientSide, args=())
			# Start the two threads
			serverThread.start()
			clientThread.start()
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)

UDPPeer()
