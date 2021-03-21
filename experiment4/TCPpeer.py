import socket
import sys, threading, time

class TCPpeer:
	"""TCP P2P Class/Object"""
	hostname = ''			# Each peer has it's own hostname
	addr = ''               # Each peer has it's own address
	peersList = []          # Each peer maintains a list of other peers addresses.add()
	ServerPort = 12000      # Each peer uses port 12000 for now?
	ClientPort = 12001      # Each peer has it's output/client side port at 12001 for now
	serverRunning = False	# Each peer has a status for it's server and client side
	clientRunning = False	# ...
	masterAddress = ''
	#peerScanRunning = False # Each peer has a status for if it is still accepting UDP broadcast messages to map other peers in network

	def broadcastHandler(self):
		try:	# Try sending broadcast to scan for other peers on network
			BroadcastS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			BroadcastS.settimeout(10)
			broadcastMessage = ' ECE369 Peer Active ' + self.addr
			#BroadcastS.sendto(broadcastMessage,('255.255.255.255', 12000))
			BroadcastS.sendto(broadcastMessage.encode(),('<broadcast>', 12000))
			print("Broadcast Sent!")
			print("Wait 10 seconds for response:")
			#self.peerScanRunning = True
			#while self.peerScanRunning:
			try:
				peerListMessage, self.masterAddress = BroadcastS.recvfrom(2048)
				self.peersList.append(peerListMessage.split(" "))
				

			#except KeyboardInterrupt:
			#	print("Keyboard Interrupt!")
			#	exit(1)
			#except TimeoutError as ex:
			#	print("Timout Exception: %s" % ex)
			#	self.peersList.remove(peer)
			#	print("Removed ", peer, " from peersList")
			except Exception as ex:		# will timeout in 10 seconds!
				ex = ''
				print("Exception: %s" % ex)
				BroadcastS.close
				#exit(1)

			
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)
		# do something, not implemented yet


	def clientSide(self):
		clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def serverSide(self):
		serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#a = 0

	def __init__(self):
		#askdfj;a
		self.hostname = socket.gethostname()
		self.addr = socket.gethostbyname(self.hostname)
		print("Hostname is: ", self.hostname)
		print("IP address is: ", self.addr)
		#self.serverRunning = True
		try:	# Try sending broadcast to scan for other peers on network
			BroadcastS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			BroadcastS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			BroadcastS.settimeout(10)
			broadcastMessage = ' ECE369 Peer Active ' + self.addr
			#BroadcastS.sendto(broadcastMessage,('255.255.255.255', 12000))
			BroadcastS.sendto(broadcastMessage.encode(),('<broadcast>', 12000))
			print("Broadcast Sent!")
			#self.peerScanRunning = True
			#while self.peerScanRunning:
			try:
				peerListMessage, self.masterAddress = BroadcastS.recvfrom(2048)
				

			except KeyboardInterrupt:
				print("Keyboard Interrupt!")
				exit(1)
			except TimeoutError as ex:
				print("Timout Exception: %s" % ex)
				#self.peersList.remove(peer)
				#print("Removed ", peer, " from peersList")
			except Exception as ex:
				ex = ''
				print("Exception: %s" % ex)
				BroadcastS.close
				#exit(1)

			
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)
			

TCPpeer()