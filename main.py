import socket
import time


def sleep_and_execute(func):
    time.sleep(60)
    return func()


def read(sock):
    data = sock.recv(4096)

    if data == '':
        raise socket.error('socket closed')
    return data

