import socket
import sys, threading

#host_name = socket.gethostname()
#IP_ADDR = socket.gethostbyname(host_name)
#print("Host name is: ", host_name)
#print("IP ADDR is: ", IP_ADDR)
#HOST = socket.get_hostbyname(socket.get_hostname())

#global server_address	# = ''
#global server_port		# = 12000
#global client_address	# = ''
#global client_port		# = 12001

#running = 1

## server side
#serverSocket = socket(AF_INET, SOCK_DGRAM)
#host = socket.gethostname(serverSocket)

#serverSocket.bind((host, local_port))
#serverSocket.bind((local_address, local_port))

#print("Host is:", host)

## client side
#clientSocket = socket(AF_INET, SOCK_DGRAM)

class UDPPeer:
	"""UDP P2P Class/Object"""
	hostname = ''			# Each peer has it's own hostname
	addr = ''               # Each peer has it's own address
	peersList = []          # Each peer maintains a list of other peers addresses.add()
	ServerPort = 12000      # Each peer uses port 12000 for now?
	ClientPort = 12001      # Each peer has it's output/client side port at 12001 for now
	serverRunning = True	# Each peer has a status for it's server and client side
	clientRunning = True	# ...
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
			broadcastMessage = bytes(' ECE369 ' + self.addr, 'utf-8')
			#BroadcastS.sendto(broadcastMessage,('255.255.255.255', 12000))
			BroadcastS.sendto(broadcastMessage,('<broadcast>', 12000))
			BroadcastS.close
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)


		try:	# Try setting up the server
			serverS=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			serverS.bind(('',self.ServerPort))
			print("ServerSide is ready to receive.")
			while self.serverRunning:
				message, clientAddress = serverS.recvfrom(2048)
				print("Message Received from: ", clientAddress)
				print(message.decode())
				ackMessage = 'Acknowledge Receipt'
				serverS.sendto(ackMessage.encode(), clientAddress)
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except Exception as ex:
			print("Exception: %s" % ex)
			exit(1)

UDPPeer()
