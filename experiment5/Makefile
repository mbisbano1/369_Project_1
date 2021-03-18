CC=gcc
CFLAGS=-Wall

all: UDPClientTimer UDPServer

UDPClientTimer: 
	$(CC) ./source/UDPClientTimer.c $(CFLAGS) -o UDPClientTimer

UDPServer:
	$(CC) ./source/UDPServer.c $(CFLAGS) -o UDPServer

clean:
	rm -r ./source/
