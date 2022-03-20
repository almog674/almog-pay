from socket import *
import time
import threading
import datetime


class Client:
    def __init__(self):
        self.IP = gethostbyname(gethostname())
        self.PORT = 11000
        self.client = self.initialize_client()
        self.new_messages = []

        recieve_thread = threading.Thread(
            target=self.recieve, args=(self.client, ))
        recieve_thread.start()

    def initialize_client(self):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((self.IP, self.PORT))
        return client

    def recieve(self, client):
        while True:
            message = client.recv(2048).decode()
            if len(self.new_messages) > 50:
                raise Exception('The data bucket is full')
            self.new_messages.append(message)

    def send_message_to_server(self, code, username, data, reciever='[SERVER]'):
        date, time = self.get_formatted_date()
        if not type(data) == str:
            data = str(data)
        full_message = f"{code}/{username}/{reciever}/{data}/{date}/{time}"
        self.client.send(full_message.encode())

    def test_auth(self):
        credentials = str(
            {'username': "almog674", 'email': 'almogmaimon674@gmail.com', 'password': 'almog290718'})
        credentials_two = str(
            {'username': "roee90", 'email': 'roee90@gmail.com', 'password': 'almog290718'})
        login = str(
            {'username': "almog674", 'password': 'almog290718'})
        self.client.send(
            f"12/guest/[SERVER]/{credentials}/19/12".encode())
        time.sleep(0.2)
        self.client.send(
            f"12/guest/[SERVER]/{credentials_two}/19/12".encode())
        time.sleep(0.2)
        self.client.send(
            f"11/guest/[SERVER]/{login}/19/12".encode())

    def test_despoit(self):
        amount = 1000
        self.client.send(
            f"21/guest/[SERVER]/{amount}/19/12".encode())

    def test_transfer(self):
        amount = 1000
        data = {"amount": amount, 'description': 'Just for fun'}
        self.client.send(
            f"23/almog674/roee90/{data}/19/12".encode())

    def get_formatted_date(self):
        date = datetime.datetime.now()
        only_date = str(date).split('.')[0]
        date, time = only_date.split(' ')
        return date, time
