
## Acess web data with Socket Library
## In this example we've taken 'www.trivago.in' as the website to scrape. 

import socket
import ssl

host = "www.trivago.in"  # Corrected host (no https://)
port = 443  # HTTPS uses port 443

# Create a socket and wrap it with SSL for HTTPS
context = ssl.create_default_context()
client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)

# Connect to the website
client_socket.connect((host, port))

# Send an HTTPS GET request
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
client_socket.send(request.encode())

# Receive response
response = b""
while True:
    data = client_socket.recv(4096)  # Read in chunks
    if not data:
        break
    response += data

# Print the response
print(response.decode(errors="ignore"))

# Close the connection
client_socket.close()
