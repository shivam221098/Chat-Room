import threading
import socket


host = 'localhost'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(50)

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            break


def receive():
    while True:
        client, address = server.accept()
        print("connected with address: {}".format(str(address)))

        client.send('YO'.encode('ascii'))
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print('Nickname of client is {}'.format(str(nickname)))
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected with server.'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()