from socket import *
import time
from time import sleep
import threading
import random
from database.db_setup import initialize_db
from database.db_tools import db_tools
from microservices.date_functions import get_formatted_date
import change_path

# Cryptography packeges
from RSA import RSA
from Three_DES import Three_des


class Server:
    def __init__(self, IP=None, PORT=11000):
        initialize_db()
        print("[SYSTEM]: database is up and ready")
        self.server = self.initialize_server(IP, PORT)
        self.db_tools = db_tools()
        self.active_clients = {}
        self.RSA = RSA()
        self.DES = Three_des()
        self.public_key, self.privet_key, self.n = self.RSA.generate_keys()
        self.key_list = self.DES.generate_keys()
        print(f"key type: {type(self.key_list[0])}")

        while True:
            time.sleep(1)
            self.handle_connection()

    def initialize_server(self, IP, PORT):
        if not IP:
            IP = self.get_host_ip()
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((IP, PORT))
        server.listen()
        print("[SYSTEM]: server is up and ready")
        return server

    def get_host_ip(self):
        hostname = gethostname()
        ip = gethostbyname(hostname)
        return ip

    def handle_connection(self):
        # 1) accept the client & add him to the active clients list
        client, address = self.server.accept()

        # 2) add the client to the client list
        # 0 = username, 1 = client, 2 = public key, 3 = n
        client_id = self.get_id()
        self.active_clients[client_id] = [None, client, None, None]

        # 3) create thread for him & start the communication
        client_thread = threading.Thread(
            target=self.handle_client, args=(client, client_id))
        client_thread.start()

        print(
            f"[SYSTEM]: there is {threading.active_count() - 1} active users!")

    def handle_client(self, client, client_id):
        time.sleep(0.05)
        # 1) ask for login/singup
        client = self.active_clients[client_id][1]

        # 2) handle messages
        while True:
            try:
                message = client.recv(1024).decode()
                if message:
                    message = self.decrypt_message(message)
                    message_code, message_sender, message_reciever, message_body, message_date, message_time = message.split(
                        '/')
                    # print(message_code, message_sender, message_reciever,
                    #       message_body, message_date, message_time)
                    if message_code == '1':
                        # Get new messages
                        pass
                    if message_code == '2':
                        # Get user information
                        self.get_user_information(client, message_sender)
                    if message_code == '11':
                        # login
                        self.login(message_body, client, client_id)
                    if message_code == '12':
                        # sinup
                        self.sign_up(message_body, client)
                    if message_code == '13':
                        # forget_password
                        pass
                    if message_code == '21':
                        # put money
                        amount = float(message_body)
                        self.unery_action(client, client_id, amount, 'despoit')
                    if message_code == '22':
                        # get money
                        amount = float(message_body)
                        self.unery_action(client, client_id, amount, 'extract')
                    if message_code == '23':
                        # Transfer money
                        self.transfer_money(
                            client, client_id, message_sender, message_reciever, message_body)
                    if message_code == '30':
                        # Get public RSA keys
                        self.update_client_key(client_id, message_body)
                    if message_code == '31':
                        # Get Three DES keys
                        self.send_encrypted_keys(client, client_id)

            except Exception as e:
                self.close_client(client, client_id)
                print(e)
                break

    def close_client(self, client, client_id):
        # remove from clients list
        self.active_clients.pop(client_id)

        # close the socket
        client.close()

    def get_id(self):
        id = ''
        for i in range(10):
            number = random.randint(0, 9)
            id += str(number)

        while id in self.active_clients.keys():
            id = self.get_id()
        return id

    def send_message_to_client(self, client, text='-', type='message', sender='[SERVER]', encryption=False):
        date, time = get_formatted_date()
        full_message = f'{sender}/{text}/{type}/{date}/{time}'
        if encryption:
            self.encrypt_and_send(client, full_message)
        else:
            client.send(full_message.encode())

    ################################# Auth Functions ###########################
    def ask_for_auth(self, client):
        self.send_message_to_client(client, 'Please Login')

    def login(self, info, client, client_id):
        info = eval(info)
        user, error = self.db_tools.login(info)
        if error:
            print("login failed")
            self.send_message_to_client(
                client, error, 'ERROR', encryption=True)
        else:
            print("login seccedd")
            self.active_clients[client_id][0] = user.username
            user = self.get_user_dict(user)
            self.send_message_to_client(
                client, str(user), type='LOGIN SUCCESS', encryption=True)

    def sign_up(self, info, client):
        info = eval(info)
        user, error = self.db_tools.signup(info)
        if not user:
            self.send_message_to_client(client, error, 'ERROR')
        else:
            message = f"Account with name {user.username} created successfuly!"
            self.send_message_to_client(client, message, type='SIGNUP SUCCESS')

    def get_user_dict(self, user):
        user = {'username': user.username, 'email': user.email,
                'account_balance': user.account_balance, 'frame': user.frame, 'all_time_high': user.all_time_high,
                'all_time_low': user.all_time_low, 'actions': self.db_tools.populate_actions(user.username, 10)}
        return user

    def check_authorize(self, client_id):
        return self.active_clients[client_id][0] != None

    ################################# Auth Functions ###########################

    ################################# Action Functions #########################
    def check_frame(self, frame, balance, amount):
        return (balance - amount) >= -frame

    def check_action(self, client_id, amount, action="extract"):
        # Check if we have user
        if not self.check_authorize(client_id):
            return 'ERROR', 'Use need to login to perform this action'
        username = self.active_clients[client_id][0]
        full_user = self.db_tools.find_user_by_name(username)[0]

        # Check if we have enought money for that
        if action == "extract" and not self.check_frame(full_user.frame, full_user.account_balance, amount):
            return 'ERROR', "You don't have enougth money for that"
        return 'Success', None

    def unery_action(self, client,  cleint_id, amount, action_type):
        '''Include all the actions for only our user like extract and despoit'''
        # Check if we allowed to do that
        status, error_message = self.check_action(
            cleint_id, amount, action=action_type)
        if status == 'ERROR':
            self.send_message_to_client(client, error_message, type=status)
            return

        # update the user in the database
        username = self.active_clients[cleint_id][0]
        new_balance = self.db_tools.unery_action_db(
            username, amount, action_type)

        # send message to user says everything okay
        self.get_user_information(client, username)
        self.send_message_to_client(
            client, f'Your new balance is {new_balance}', type='SUCCESS')

    def transfer_money(self, client, client_id, sender, reciever, data):
        # Extract  the data
        data = eval(data)
        amount = data['amount']
        description = data['description']

        # Check if the sender is able to perform this
        status, error_message = self.check_action(client_id, amount)
        if status == 'ERROR':
            self.send_message_to_client(client, error_message, status)
            return

        new_sender_balance, new_reciever_balance, error = self.db_tools.transfer_money(
            sender, reciever, amount, description)
        print(f'error: {error}')
        if error:
            return self.send_message_to_client(
                client, error, type='ERROR')

        # send messages to confirm
        self.get_user_information(client, sender)
        self.send_message_to_client(
            client, f'Transfer to {reciever} {amount} dollars', type='SUCCESS')

    ################################# Action Functions #########################

    ################################# Information Functions #########################
    def get_user_information(self, client, username):
        user = self.db_tools.find_user_by_name(username)[0]
        user_to_send = self.get_user_dict(user)
        self.send_message_to_client(client, str(user_to_send), 'USER')

    ################################# Information Functions #########################

    ################################# cryptography Functions #########################
    def update_client_key(self, client_id, data):
        data = eval(data)
        key = data['key']
        n = data['n']
        self.active_clients[client_id][2] = key
        self.active_clients[client_id][3] = n

    def send_encrypted_keys(self, client, client_id):
        public_key = self.active_clients[client_id][2]
        n = self.active_clients[client_id][3]
        encrypted_keys = []
        for i in range(len(self.key_list)):
            key = self.RSA.encrypt(public_key, n, self.key_list[i])
            encrypted_keys.append(key)
        print(self.key_list)
        self.send_message_to_client(client, str(encrypted_keys), '[KEYS]')

    def encrypt_and_send(self, client, msg):
        (iv, cipher_text) = self.DES.encrypt(msg, self.key_list)
        full_message = f'[SERVER_ENCRYPT] {cipher_text}#{iv}'
        client.send(full_message.encode())

    def decrypt_message(self, message):
        encrypted, content = message.split("#", 1)
        if encrypted == '0':
            return content
        cipher_text, IV = content.split("#", 1)
        plain_text = self.DES.decrypt(cipher_text, self.key_list, IV)
        return plain_text
    ################################# cryptography Functions #########################


my_server = Server()
