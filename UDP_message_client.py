import socket
msgFromClient       = " 6405003317 Jutharat Pooamorn"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.1.43", 12000)
buffer_Size          = 2048
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(buffer_Size)
msg =  format(msgFromServer[0])
print(msg)