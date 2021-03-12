#include <stdio.h>
#define CR printf("\n")
#define DEFAULT_PORT 12000

int main(int argc, char * argv[])
{
	unsigned int serverPort;

	if (argc == 2)
	{
		/*convert input string to int*/
		if (sscanf(argv[1], "%u", &serverPort) == 1)
		{
			printf("Successfully converted to int %d" , serverPort); CR; 
		}
		else
		{
			printf("Error: Input value not an integer. Exiting."); CR; 
			return(1);
		}
	}
	else
	{
		printf("Usage: ./UDPServer.c server_port"); CR; 
		printf("Using default server port value of %d", DEFAULT_PORT); CR; 
		serverPort=DEFAULT_PORT;
	}


	return(0);
}
