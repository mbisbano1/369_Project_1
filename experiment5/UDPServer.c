#include <stdio.h>
#define CR printf("\n")

int main(int argc, char * argv[])
{
	if (argc != 2)
	{
		printf("Usage: ./UDPServer.c server_port"); CR; 
		return(1);
	}

	printf("You entered a server port value of %s", argv[1]); CR;

	return(0);
}
