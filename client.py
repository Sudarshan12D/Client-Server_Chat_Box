#client.py
import socket

port = 12345

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create an INET, STREAMing socket
clientsocket.connect(('localhost', port)) # to connect client socket to my host and the port

user1_name = input("Enter User 1's name: ") #input client name
clientsocket.send(user1_name.encode('utf-8')) #sending the user 1 name to server

user2_name = clientsocket.recv(1024).decode('utf-8')  # receiving user2's name
print(f"User 2's name: {user2_name}.\n")

def start1():
     
    while True:
        
        message = input(f"  {user1_name}: ") #to send message to server
        clientsocket.send(message.encode('utf-8'))
        if message.lower() == "bye":
            print(f"\n{user1_name} left..")
            clientsocket.close() #closing the socket when bye is called
            print(f"Client connection closed..")
            print(".......LA FIN.......")
            break
        
        reply = clientsocket.recv(1024).decode('utf-8') #receiving reply from server
        print('\033[1m' + f"  {user2_name} replied: {reply}" + '\033[0m') #to print the message sent by server
        if reply.lower() == "bye":
            print(f"\n{user2_name} left..") 
            clientsocket.close() #closing the socket when bye is called
            print(f"Client connection closed..")
            print(".......LA FIN.......")
            break
    
if __name__ == "__main__":
    start1()
