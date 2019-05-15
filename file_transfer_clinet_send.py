import socket
import os

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#file name
filename = input("Input your file name : ")
#total file size
totalSize = os.path.getsize(filename)

sendIp = "192.168.56.1";

f = open(filename, 'rb');

#total file size, file name send
socket.sendto(filename.encode(), (sendIp, 9000))
socket.sendto(str(totalSize).encode(), (sendIp, 9000))

#start file transmit
print("File transmit Start...")

currentSize = 0
for i in range(int(totalSize/1024)+1):
    data = f.read(1024)
    socket.sendto(data, (sendIp,9000))
    currentSize += len(data)
    print("current_size / total_size = ", currentSize, "/", totalSize, ", ", (currentSize / totalSize) * 100, "%" )

if currentSize == totalSize:
    print("ok")

print("file_send_end")
f.close()
