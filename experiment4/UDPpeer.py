from socket import *
import sys, threading


host_name = socket.gethostname()
IP_ADDR = socket.gethostbyname(host_name)
print("Host name is: ", host_name)
print("IP ADDR is: ", IP_ADDR)
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
	addr = ''               # Each peer has it's own address
	peersList = []          # Each peer maintains a list of other peers addresses.add()
	ServerPort = 12000      # Each peer uses port 12000 for now?
	ClientPort = 12001      # Each peer has it's output/client side port at 12001 for now
	def __init__(self):
		self.addr = input("Enter your IP Address from ifconfig: eg. 192.168.0.150")

		try:	# Try sending broadcast to scan for other peers on network
			BroadcastS=socket(AF_INET, SOCK_DGRAM)
			BroadcastS.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
			broadcastMessage = 'P2P_Messenger_Active' + self.addr
			BroadcastS.sendto(broadcastMessage,('255.255.255.255', 12000))
			BroadcastS.close
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except:
			print("error sending broadcast message")
			exit(1)
		try:	# Try setting up the server
			serverS=socket(AF_INET, SOCK_DGRAM)
			serverS.bind(('',self.ServerPort))
			print("ServerSide is ready to receive.")
		except KeyboardInterrupt:
			print("Keyboard Interrupt!")
			exit(1)
		except:
			print("Server unable to be bound")
			exit(1)

UDPPeer()
