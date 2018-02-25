# Import socket library
from socket import *

# Define server hostname / IP and port
serverName = '127.0.0.1'
serverPort = 12001

# Create client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server socket
clientSocket.connect((serverName, serverPort))

# Parse user input
sentence = raw_input('Input lowercase sentence: ')

# Send user input
clientSocket.send(sentence)

# Receive response from server
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence

# Close connection
clientSocket.close()
