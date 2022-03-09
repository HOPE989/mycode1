#!/usr/bin/python
from socket import *
import struct
import os


class Client:
    def __init__(self, ip, port):
        self.tcp_socket_client: socket = None
        self.ip = ip
        self.port = port

    def tcp_connect(self):
        self.tcp_socket_client = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket_client.connect((self.ip, self.port))
        return self.tcp_socket_client

    def send_command(self):
        while True:
            command = input()
            self.send_train(command.encode('utf8'))
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd()
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm()
            elif command[:4] == 'gets':
                self.do_gets()
            elif command[:4] == 'puts':
                self.do_puts(command)
            else:
                print('wrong command!')

    def send_train(self, send_bytes):
        """
        以火车头加身体的形式发
        :param send_bytes:
        :return:
        """
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.tcp_socket_client.send(train_head_bytes + send_bytes)

    def recv_train(self):
        train_head_bytes = self.tcp_socket_client.recv(4)
        train_head = struct.unpack('I', train_head_bytes)
        return self.tcp_socket_client.recv(train_head[0])

    def do_ls(self):
        print(self.recv_train().decode('utf8'))

    def do_cd(self):
        print(self.recv_train().decode('utf8'))

    def do_pwd(self):
        print(self.recv_train().decode('utf8'))

    def do_rm(self):
        print(self.recv_train().decode('utf8'))

    def do_gets(self):
        file_name = self.recv_train().decode('utf8')
        if file_name != 'No such file!':
            file = open(file_name, 'wb')
            file.write(self.recv_train())
            file.close()
        else:
            print(file_name)

    def do_puts(self, command: str):
        try:
            file_name = command.split()[1]
            file = open(file_name, 'rb')
            self.send_train(file_name.encode('utf8'))
            content = file.read()
            self.send_train(content)
            file.close()
        except FileNotFoundError:
            self.send_train('-1'.encode('utf8'))
            print('No such file!')


if __name__ == '__main__':
    c = Client('192.168.238.128', 2012)
    c.tcp_connect()
    c.send_command()
