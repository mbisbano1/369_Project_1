/*https://www.educative.io/edpresso/how-to-implement-udp-sockets-in-c*/
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>

#define CR printf("\n")
#define MAX_MESSAGE_SIZE 2048

int udpClient(char * serverAddress, int serverPort) 
{

	unsigned long int i;
	int socketDescriptor;
	struct sockaddr_in server_addr;
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
		printf("Error: could not create socket."); CR; 
		return(1);
	}

	/*set server attributes*/
	server_addr.sin_family=AF_INET;
	server_addr.sin_port=serverPort;
	server_addr.sin_addr.s_addr=inet_addr(serverAddress);
	
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
			printf("Error: could not send message."); CR; 
			return(1);
		}

		/*listen for response*/
		if (recvfrom(socketDescriptor, messageFromServer, sizeof(messageFromServer), 0, \
			(struct sockaddr*)&server_addr, &serverStructLength) < 0)
		{
			printf("Error: could not receive message."); CR;
			return(1);
		}

		/*end timer and calculate total time*/
		totalTime=(long int)(clock() - startTime);

		printf("[Response in %ld RTT] %s", totalTime, messageFromServer); 
	}
}

int main(void)
{
	udpClient("127.0.0.1", 12000);
	return(0);
}

