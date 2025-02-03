import socket

# Connect to the server
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Send the HTTP GET request for the URL
request = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'
mysock.send(request.encode())

# Receive the response
response = mysock.recv(1024)
while len(response) > 0:
    print(response.decode())
    response = mysock.recv(1024)

# Close the socket
mysock.close()

'''


Client (Your Machine)                             Network                                 Server (Remote Machine)
------------------------                       -------------                           ----------------------------
[Text] --> (Encode) --> [Bytes] -->          (Send via socket)--> [Network]          --> [Bytes] --> (Decode) --> [Text]



'''