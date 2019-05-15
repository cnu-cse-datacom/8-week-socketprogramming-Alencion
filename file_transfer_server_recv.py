import socket

#communicate
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9000))

#filename, totalSize get
filenameByte, addr = server_socket.recvfrom(1024)
totalSizeByte, addr = server_socket.recvfrom(1024)

#decode filename, totalSize
filename = filenameByte.decode()
totalSize = int(totalSizeByte.decode())

print("File Name : ", filename)
print("File Size : ", totalSize)

f = open(filename, 'wb')

currentSize = 0
for i in range(int(totalSize/1024)+1):
    data, addr = server_socket.recvfrom(1024)
    currentSize += len(data)
    f.write(data)
    print("current_size / total_size = ", currentSize, "/", totalSize, ", ", (currentSize / totalSize) * 100, "%" )

f.close()
