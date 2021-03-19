#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define DEFAULT_PORT 12000
#define DEFAULT_IP "127.0.0.1"
#define MAX_MESSAGE_LENGTH 2048
#define CR printf("\n")


int serverLoop(int serverPort)
{
	int socketDescriptor;
	unsigned long int i;
	char receivedClientMessage[MAX_MESSAGE_LENGTH];
	struct sockaddr_in server_addr, client_addr;
	unsigned int clientStructLength=sizeof(client_addr);

	/*clear string*/
	for (i=0; i<MAX_MESSAGE_LENGTH; i++)
	{
		receivedClientMessage[i]='\0';
	}

	/*open socket*/
	socketDescriptor=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (socketDescriptor < 0)
	{
		printf("Error: could not create socket."); CR; 
		return(1);
	}

	/*set socket library settings*/
	server_addr.sin_family=AF_INET;
	server_addr.sin_port=serverPort;
	server_addr.sin_addr.s_addr=inet_addr(DEFAULT_IP);

	/*bind*/
	if (bind(socketDescriptor, (struct sockaddr*)&server_addr, sizeof(server_addr)))
	{
		printf("Error: could not bind to port."); CR;
		return(1);
	}

	printf("Now listening for messages..."); CR; 
	while(1)
	{
		/*listen*/
		if (recvfrom(socketDescriptor, receivedClientMessage, sizeof(receivedClientMessage), 0, \
			(struct sockaddr*)&client_addr, &clientStructLength) < 0)
		{
			printf("Error: could not receive data from client."); CR; 
			return(1);
		}

		/*have message, now send back uppercase version*/
		printf("[%s:%i] %s", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port), receivedClientMessage); 
		for(i=0; i<MAX_MESSAGE_LENGTH; i++)
		{
			if (receivedClientMessage[i] >= 'a' && receivedClientMessage[i] <= 'z')
			{
				receivedClientMessage[i] -= 'a' - 'A';
			}
		}

		/*send uppercase string to client*/
		if (sendto(socketDescriptor, receivedClientMessage, sizeof(receivedClientMessage), 0, \
			(struct sockaddr*)&client_addr, clientStructLength) < 0)
		{
			printf("Error: could not send data to client."); CR; 
			return(1);
		}
	}
}

int main(int argc, char * argv[])
{
	unsigned int serverPort;

	if (argc == 2)
	{
		/*convert input string to int*/
		if (sscanf(argv[1], "%u", &serverPort) != 1)
		{
			printf("Error: Input value not an integer. Quitting."); CR; 
			return 1;
		}
	}
	else
	{
		printf("Usage: ./UDPServer.c server_port"); CR; 
		printf("Using default server port value of %d", DEFAULT_PORT); CR; 
		serverPort=DEFAULT_PORT;
	}

	return(serverLoop(serverPort));
}

