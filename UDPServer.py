from socket import *

#Use your own IP address here
serverIP="127.0.0.1"
serverPort=55000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((serverIP,serverPort))
print "Ready to serve"

while 1:

	message,clientAddress=serverSocket.recvfrom(2048)
	modifiedMessage="Welcome "+ message.upper() + " from BSCS7C"
	serverSocket.sendto(modifiedMessage,clientAddress)
	print message
