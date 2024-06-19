import socket
import time
def server(host = 'localhost', port=8082):
    
    #The maximum amount of data to be received at once
    data_payload = 2048 
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    i = 0
    while True: 
        print ("Waiting to receive message from client")        
        client, address = sock.accept()
        data = client.recv(data_payload) 
        if data:
            with open("log.txt","a") as file:
                file.write(f"<{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}:({address[0]})>:'{data.decode('utf-8')}' \n")
            print (f"Data: '{data.decode('utf-8')}'")
            client.send(data)
            print (f"sent '{data.decode('utf-8')}' bytes back to {address}")
            # end connection
            client.close()
            
            i+=1
            if i>=3: break           
server()