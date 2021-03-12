/*https://www.binarytides.com/socket-programming-c-linux-tutorial*/
#include <stdio.h>
#include <sys/socket.h>
#define CR printf("\n")
#define DEFAULT_PORT 12000

int serverLoop(int serverPort)
{
	int socketDescriptor;

	struct in_addr
	{
		unsigned long s_addr;
	};

	struct sockaddr_in
	{
		short sin_family;
		unsigned short sin_port;
		struct in_addr sin_addr;
		char sin_zero[8];
	};

	struct sockaddr
	{
		unsigned short sa_family;
		char sa_data[14];

	};


	socketDescriptor=socket(AF_INET, SOCK_STREAM, 0);
	if (socketDescriptor == -1)
	{
		printf("Error: Could not create socket. Quitting."); CR; 
		return(1);
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
