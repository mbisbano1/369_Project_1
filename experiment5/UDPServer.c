#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netinet/in.h>
#include <errno.h>

#define DEFAULT_PORT 12000
#define CR printf("\n")

int serverLoop(int serverPort)
{
	struct sockaddr_in server_addr, client_addr;




	server_addr.sin_family=AF_INET;
	server_addr.sin_port=htons(serverPort);
	server_addr.sin_addr.s_addr=INADDR_ANY;



	return(0);
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
			return(1);
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

