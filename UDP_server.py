import socket
localIP     = "192.168.1.43"
localPort   = 12000
buffer_Size  = 2048
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(buffer_Size)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client : {}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    UDPServerSocket.sendto(bytesToSend, address)