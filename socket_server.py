#server.py
import socket
import logging
import socket_UI



def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket
        addr = ('自家IP', 5000)
        s.bind(addr)  #將IP與PORT連接
        
        s.listen()
        s, addr = s.accept()
        print(f'[Listening] Server is listening on {addr}.')

        try:
            ann = '來自client' + str(addr)

            receive_data, addr = s.recvfrom(1024)
            print(ann)
            print(receive_data.decode('utf-8'))
            if "exit" in receive_data.decode('utf-8'):
                s.send('You have exited the server.'.encode('utf-8'))
            else:
                msg = input('please input send to msg:')
                s.send(msg.encode('utf-8'))

        except ConnectionResetError:
            logging.warning('Someone left unexcept.')

if __name__ == '__main__':
    print('server is starting.')

    main()


