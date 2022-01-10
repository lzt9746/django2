from django.test import TestCase

# Create your tests here.

import paramiko


class Webssh():
    def __init__(self, host, username, password, ):
        self.host = host
        self.username = username
        self.password = password

    def client_ssh(self, cmd):
        sh = paramiko.SSHClient()
        sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sh.connect(self.host, username=self.username, password=self.password)
        stdin, stdout, stderr = sh.exec_command(cmd)
        right_info = stdout.read()
        err_info = stderr.read()

        if right_info:
            print(right_info.decode('utf-8'))
        elif err_info:
            print(err_info.decode('utf-8'))
        else:
            print("success")


if __name__ == '__main__':
    a = Webssh('192.168.192.129', 'root', '974672675')
    while True:
        command = input("$:")
        a.client_ssh(command)
