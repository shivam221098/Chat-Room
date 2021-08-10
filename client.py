import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 55555))
nickname = input("Nickname: ")


def receive():
    while True:
        try:
            message = client.recv(1024)
            if message.decode('ascii') == "YO":
                pass
            else:
                print(message.decode('ascii'))

        except:
            print("Something went wrong.")
            client.close()
            break


def write():
    message = f'{nickname}: {input("")}'
    client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

