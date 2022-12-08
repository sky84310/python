# client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    while True:

        host = '自家IP'
        port = 5000

        input_data = input('please input msg:')
        send_data = input_data.encode('utf-8')

        s.send(send_data)

        # s.sendto(send_data.encode('utf-8'),(host,port))

        msg, addr = s.recv(1024)
        print("來自伺服器" + str(addr) + "的訊息:")
        print(msg.decode('utf-8'))
        if msg.decode('utf-8').lower() == 'EXIT'.lower():
            break
except:
    s.close()
