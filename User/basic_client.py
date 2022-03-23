from socket import *
import time
import threading
import datetime

import change_path

from RSA import RSA
from Three_DES import Three_des


class Client:
    def __init__(self):
        self.IP = gethostbyname(gethostname())
        self.PORT = 11000
        self.client = self.initialize_client()
        self.new_messages = []

        # Initialize cryptography tools
        self.RSA = RSA()
        self.DES = Three_des()

        self.public_key, self.privet_key, self.n = self.RSA.generate_keys()
        self.des_keys = []
        self.send_rsa_key()
        time.sleep(0.1)
        self.ask_for_des_keys()

        recieve_thread = threading.Thread(
            target=self.recieve, args=(self.client, ))
        recieve_thread.start()

    def initialize_client(self):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((self.IP, self.PORT))
        return client

    def recieve(self, client):
        while True:
            message = client.recv(4096).decode()
            if len(self.new_messages) > 50:
                raise Exception('The data bucket is full')
            self.new_messages.append(message)

    def decrypt_message(self, message):
        _, message_content = message.split(" ", 1)
        cipher_text, iv = message_content.split("#")
        plain_text = self.DES.decrypt(cipher_text, self.des_keys, iv)
        return plain_text

    def check_dictionary(self, message):
        if ":" in message and message[0] != '{':
            print("fixing the dictionary")
            message = "{" + message
        return message

    def send_message_to_server(self, code, username, data, reciever='[SERVER]', encrypted=True):
        date, time = self.get_formatted_date()
        if not type(data) == str:
            data = str(data)
        full_content = f"{code}/{username}/{reciever}/{data}/{date}/{time}"
        if encrypted:
            iv, cipher_message = self.DES.encrypt(full_content, self.des_keys)
            full_message = f"1#{cipher_message}#{iv}"
        else:
            full_message = f"0#{full_content}"
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

    def send_rsa_key(self):
        data = {"key": self.public_key, "n": self.n}
        self.client.send(
            f"0#30/almog674/[SERVER]/{data}/19/12".encode())

    def ask_for_des_keys(self):
        self.client.send(
            f"0#31/almog674/[SERVER]/data/19/12".encode())

    def try_encypted_message(self):
        pass

    def get_keys(self, keys):
        for key in keys:
            key = self.RSA.decrypt(self.privet_key, self.n, key)
            self.des_keys.append(key)
            print(key)
