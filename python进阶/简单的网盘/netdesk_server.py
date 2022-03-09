#!/usr/bin/python
from socket import *
import struct
import os


class Server:
    def __init__(self, ip, port):
        self.tcp_socket_server: socket = None
        self.ip = ip
        self.port = port

    def tcp_init(self):
        self.tcp_socket_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket_server.bind((self.ip, self.port))
        self.tcp_socket_server.listen(128)

    def task(self):
        new_client, client_addr = self.tcp_socket_server.accept()
        user = User(new_client)
        user.deal_command()


class User:
    """
    一个用户对应一个user对应一个客户端
    """

    def __init__(self, new_client):
        self.new_client: socket = new_client
        self.user_name = None
        self.path = os.getcwd()

    def deal_command(self):
        while True:
            command = self.recv_train().decode('utf8')
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd(command)
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm(command)
            elif command[:4] == 'gets':
                self.do_gets(command)
            elif command[:4] == 'puts':
                self.do_puts()
            else:
                print('wrong command!')

    def send_train(self, send_bytes):
        """
        以火车头加身体的形式发
        :param send_bytes:
        :return:
        """
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.new_client.send(train_head_bytes + send_bytes)

    def recv_train(self):
        train_head_bytes = self.new_client.recv(4)
        train_head = struct.unpack('I', train_head_bytes)
        return self.new_client.recv(train_head[0])

    def do_ls(self):
        data = ''
        for file in os.listdir(self.path):
            data += file + ' ' * 5 + str(os.stat(file).st_size) + '\n'
        self.send_train(data.encode('utf8'))

    def do_cd(self, command: str):
        path = command.split()[1]
        os.chdir(path)
        self.path = os.getcwd()
        self.send_train(self.path.encode('utf8'))

    def do_pwd(self):
        self.send_train(self.path.encode('utf8'))

    def do_rm(self, command: str):
        rm_file = command.split()[1]
        try:
            os.remove(rm_file)
            self.send_train((rm_file + ' deleted!').encode('utf8'))
        except FileNotFoundError:
            self.send_train('No such file!'.encode('utf8'))

    def do_gets(self, command: str):
        file_name = command.split()[1]
        try:
            file = open(file_name, 'rb')
            self.send_train(file_name.encode('utf8'))
            content = file.read()
            self.send_train(content)
            file.close()
        except FileNotFoundError:
            print('No such file!')
            self.send_train('No such file!'.encode('utf8'))

    def do_puts(self):
        file_name = self.recv_train().decode('utf8')
        if file_name == '-1':
            pass
        else:
            file = open(file_name, 'wb')
            file.write(self.recv_train())
            file.close()


if __name__ == '__main__':
    s = Server('', 2012)
    s.tcp_init()
    s.task()
