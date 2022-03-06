from socket import *


class Socket_Server:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def initialize_server(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((self.IP, self.PORT))
        server.listen()
        print("")
        return server
