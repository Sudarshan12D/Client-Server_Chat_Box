#server.py
import socket
port = 12345
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create an INET, STREAMing socket
serversocket.bind(('localhost', port)) # bind the socket to a public host, and a well-known port
serversocket.listen() # become a server socket

print("Waiting for Clients to connect...") # Client not connect yet
(clientsend, address) = serversocket.accept() #accepting client connection

user1_name = clientsend.recv(1024).decode('utf-8') # receiving user1's name
print(f"Client({user1_name}) with the address: {address} has connected.\n") #prints the client connected

user2_name = input("Enter user 2's name: ") #writing User2 (server) name
print(f"User 1's name: {user1_name}.\n")
clientsend.send(user2_name.encode('utf-8')) #sending the user_2 name to client

def start():
    connection = True # to close connnection when by is called
    while connection == True:
        
        reply = clientsend.recv(1024).decode('utf-8') #receiving reply from client
        print('\033[1m' + f"  {user1_name} replied: {reply}"+'\033[0m') #to print the message sent by client
        if reply.lower() == "bye": 
            print(f"\n{user1_name} left..") #client left
            connection = False # to close connection when bye is said
            break

        message = input(f"  {user2_name}: ") #to send message to client
        clientsend.send(message.encode('utf-8'))
        if message.lower() == "bye":
            print(f"\n{user2_name} left..") #server left
            connection = False
            break

    if connection == False:
        clientsend.close()
        serversocket.close() #closing the sockets
        print(f"Server connection closed..")
        print(".......LA FIN.......")
        exit()

if __name__ == "__main__":
    start()



            