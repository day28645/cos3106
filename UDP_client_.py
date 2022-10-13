from socket import *
serverAddressPort = ('localhost' , 12000)
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Input lowercase sentence: ")
clientSocket.sendto(str.encode(message),(serverAddressPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ("From Server :",modifiedMessage.decode())
clientSocket.close()