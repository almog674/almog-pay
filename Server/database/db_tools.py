import mongoengine
from email import message
from models.user import User
from models.Action import Action
from models.Message import Message


class db_tools:
    def __init__(self):
        # self.delete_all_users()
        self.print_all_users()

    def signup(self, info):
        # Extract the information
        username = info['username']
        email = info['email']
        password = info['password']

        # Error handling
        users_with_name = self.find_user_by_name(username)
        users_with_email = self.find_user_by_email(email)
        if len(users_with_name) > 0:
            return None, 'The username is already have been taken'
        if len(users_with_email) > 0:
            return None, 'The email is already have been used'

        # Create the user
        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.password = password
        try:
            new_user.save()
        except mongoengine.errors.ValidationError as e:
            return None, str(e)

        return new_user, None

    def login(self, info):
        username = info['username']
        password = info['password']

        users_with_name = self.find_user_by_name(username)
        if len(users_with_name) == 0:
            return None, f'There is no user with the name: {username}'
        user = users_with_name[0]
        if user.password != password:
            return None, f'The passowrd is incorrect'

        return user, None

    def unery_action_db(self, username, amount, type='despoit'):
        '''Include all the actions for only our user like extract and despoit'''
        user = self.find_user_by_name(username)[0]
        user = self.create_action(user, type, amount)
        if type == 'extract':
            amount = -amount
        new_balance = self.update_balance(user, amount)
        for action in user.actions:
            action = Action.objects(id=action)[0]
            print(action.action_type, action.amount, action.time)
        return new_balance

    def create_action(self, user, type, amount, description=''):
        new_action = Action()
        new_action.action_type = type
        new_action.amount = amount
        new_action.description = description
        new_action.save()
        user.actions.append(new_action.id)
        return user

    def create_message(self, user, description):
        message = Message()
        message.description = description
        message.save()
        user.inbox.append(message.id)
        return user

    def delete_all_users(self):
        all_users = User.objects()
        all_users.delete()

    def update_balance(self, user, amount):
        user.account_balance += amount
        user.save()
        return user.account_balance

    def transfer_money(self, sender, reciever, amount, description):
        sender_user = self.find_user_by_name(sender)[0]
        reciever_user = self.find_user_by_name(reciever)[0]

        if not reciever_user:
            return 'ERROR', f'the user {reciever} is not exits'

        # Handle sender
        sender_user = self.create_action(
            sender_user, f'Transfer to {reciever}', amount, description=description)
        new_sender_balance = self.update_balance(sender_user, -amount)

        # Handle reciever
        reciever_user = self.create_action(
            reciever_user, f'Recieve from {sender}', amount, description=description)
        message_text = f'You have recieved {amount} from {sender}'
        reciever_user = self.create_message(reciever, message_text)
        new_reciever_balance = self.update_balance(reciever_user, amount)

        return new_sender_balance, new_reciever_balance

    def print_all_users(self):
        all_users = User.objects()
        for user in all_users:
            print("#################")
            print(f'name: {user.username}')
            print(f"email: {user.email}")
            print(f"password: {user.password}")

    def populate_actions(self, name, number):
        # Get the last 10 actions of the user
        items = User.objects(username=name)[0].actions
        if len(items) > number:
            items = items[len(items) - number::]
        return items

    def find_user_by_name(self, username):
        user = User.objects(username=username)
        return user

    def find_user_by_email(self, email):
        user = User.objects(email=email)
        return user
