from socket import *
import time
#use the IP address of your neighbor running the server
serverName="127.0.0.1"
serverPort=55000

clientSocket = socket(AF_INET,SOCK_DGRAM)

#use your name here
message="kaleem ullah"


clientSocket.sendto(message,(serverName,serverPort)) 

modifiedMessage,serverAddress=clientSocket.recvfrom(2048)

4
print("received from")
for n in serverAddress:
	print(n)
print(modifiedMessage)
send_time_ms = time.time()
# sending the packet
# ...
# receiving the packet
recv_time_ms = time.time()
rtt_in_ms = round(recv_time_ms - send_time_ms, 3)
print(rtt_in_ms)
clientSocket.close()


