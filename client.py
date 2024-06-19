
import socket
def client(host = 'localhost', port=8082):
    i = 0
    while True:
       
       if i>=3:break
       message = input("Escreva:")
        # Create a TCP/IP socket 
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        # Connect the socket to the server 
       server_address = (host, port) 
       print ("Connecting to %s port %s" % server_address)     
        # Send data 
       sock.connect(server_address)        
       try:
        # Send data            
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Received:'%s'" % data.decode('utf-8'))
       except socket.error as e: 
            print ("Socket error: %s" %str(e)) 
       except Exception as e: 
            print ("Other exception: %s" %str(e)) 
       finally: 
            print ("Closing connection to the server") 
            sock.close()
            i+=1            
client()