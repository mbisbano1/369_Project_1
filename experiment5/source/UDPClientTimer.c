/*https://www.educative.io/edpresso/how-to-implement-udp-sockets-in-c*/
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>

#define CR printf("\n")
#define MAX_MESSAGE_SIZE 2048

int UDPClientTimer(char * serverAddress, int serverPort) 
{
	unsigned long int i;
	int socketDescriptor;
	struct sockaddr_in server_addr;
	struct timeval timeVal;
	unsigned int serverStructLength=sizeof(server_addr);
	char messageFromServer[MAX_MESSAGE_SIZE];
	char messageToSend[MAX_MESSAGE_SIZE];
	clock_t startTime;
	clock_t totalTime;

	/*clear strings*/
	for(i=0; i<MAX_MESSAGE_SIZE; i++)
	{
		messageToSend[i]='\0';
		messageFromServer[i]='\0';
	}

	/*open socket*/
	socketDescriptor=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (socketDescriptor < 0)
	{
		printf("[ERROR] could not create socket."); CR; 
		return(1);
	}

	/*set server attributes*/
	server_addr.sin_family=AF_INET;
	server_addr.sin_port=serverPort;
	server_addr.sin_addr.s_addr=inet_addr(serverAddress);

	/*set timeout*/
	timeVal.tv_sec=10;
	if (setsockopt(socketDescriptor, SOL_SOCKET, SO_RCVTIMEO, &timeVal, sizeof(timeVal)) < 0)
	{
		printf("[ERROR] could not set timeout value."); CR;
	}

	
	while (1)
	{
		/*get message*/
		printf("Enter a message: ");
		fgets(messageToSend, MAX_MESSAGE_SIZE, stdin);

		/*start timer*/
		startTime=clock();

		/*send to server*/
		if (sendto(socketDescriptor, messageToSend, sizeof(messageToSend), 0, \
			(struct sockaddr*)&server_addr, serverStructLength) < 0)
		{
			printf("[ERROR] Send timed out."); CR; 
			return(1);
		}

		/*listen for response*/
		if (recvfrom(socketDescriptor, messageFromServer, sizeof(messageFromServer), 0, \
			(struct sockaddr*)&server_addr, &serverStructLength) < 0)
		{
			printf("[ERROR] Receive timed out."); CR;
			return(1);
		}

		/*end timer and calculate total time*/
		totalTime=(long int)(clock() - startTime);

		printf("[Response in %ld clock cycles] %s", totalTime, messageFromServer); 
	}
}

int main(int argc, char * argv[])
{
	unsigned int serverPort;

	if (argc == 3)
	{
		/*convert port number to int*/
		if (sscanf(argv[2], "%u", &serverPort) != 1)
		{
			printf("[ERROR] input value invalid."); CR;
			return(1);
		}

		return(UDPClientTimer(argv[1], serverPort));
	}
	else
	{
		printf("Usage: ./UDPClient server_address server_port"); CR;
		return(1);
	}
}
