from socket import *
import pickle as rick
from time import time


class Connection:
    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.host = "localhost"
        self.port = 3565
        self.address = (self.host, self.port)
        
        self.board = self.connect()
        self.board = rick.loads(self.board)

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(4096*8)
        except error as e:
            print(e)


    def disconnect(self):
        try:
            self.client.close()
            return 'great success'
        except error as e:
            print(e)
            
    def send(self, data, pick=False):
        timer = time()
        while time() - timer < 5:
            try:
                if pick:
                    self.client.send(rick.dumps(data))
                else:
                    self.client.send(str.encode(data))
                reply = self.client.recv(4096*8)
                try:
                    reply = rick.loads(reply)
                    break
                except Exception as e:
                    print(e)

            except error as e:
                print(e)
        return reply
        