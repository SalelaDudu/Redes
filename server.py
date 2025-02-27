import threading
import socket
import time

# Lista de clientes conectados ao servidor
clients = []

# Função para lidar com as mensagens de um cliente
def handle_client(client):
  while True:
      try:
            msg = client.recv(2048)
            with open("log.txt","a") as file:
                file.write(f"<{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}:({client.getpeername()[0]})>:'{msg.decode('utf-8')}' \n")
            broadcast(msg, client)
      except:
          remove_client(client)
          break

# Função para transmitir mensagens para todos os clientes
def broadcast(msg, sender):
  for client in clients:
      if client != sender:
          try:                
                client.send(msg)            
          except:
                remove_client(client)

# Função para remover um cliente da lista
def remove_client(client):
  clients.remove(client)

# Função principal
def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  print("Iniciou o servidor de bate-papo")

  try:
      server.bind(("191.52.5.175", 7777))
      server.listen()
  except:
      return print('\nNão foi possível iniciar o servidor!\n')

  while True:
      client, addr = server.accept()
      clients.append(client)
      print(f'Cliente conectado com sucesso. IP: {addr}')

      # Inicia uma nova thread para lidar com as mensagens do cliente
      thread = threading.Thread(target=handle_client, args=(client,))
      thread.start()      

# Executa o programa
main()
