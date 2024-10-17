import socket
import threading
IP='0.0.0.0'
PORT=9998
def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')
    def handle_client(client_socket):
        with client_socket as sock:
            request=sock.recv(1042)
            print(f'[*] recived: {request.decode("utf-8")}')
            sock.send(b'ACK')
            #this one needed to be defined so i duplicated so it work sorry for being dirty
    while True:
        client,address=server.accept()
        print(f'[*]Accepted conection from {address[0]}:{address[1]}')
        client_handler=threading.Thread(target=handle_client,args=(client, ))
        client_handler.start()
        def handle_client(client_socket):
            with client_socket as sock:
                request=sock.recv(1042)
                print(f'[*] recived: {request.decode("utf-8")}')
                sock.send(b'ACK')
if __name__=='__main__':
    main()
