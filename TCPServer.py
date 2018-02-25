# Import socket library
from socket import *

# Define server port
serverPort = 12001

# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associate socket with IP address
serverSocket.bind(('', serverPort))

# Listen for requests
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
    # Accept request
    connectionSocket, addr = serverSocket.accept()

    # Convert lowercase input to uppercase
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()

    # Send response to client
    connectionSocket.send(capitalizedSentence)

    # Close connection
    connectionSocket.close()
