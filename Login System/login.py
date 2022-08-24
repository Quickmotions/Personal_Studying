# 24/08/2022 - Fergus Haak - Login System
import pickle


# TODO: combine with old GUI based login system
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


def load_users() -> dict[str:User]:
    with open("data/users.pickle", "rb") as f:
        return pickle.load(f)


class UserManager:
    def __init__(self):
        self.users = load_users()

    def new_user(self, name: str, password: str):
        self.users[name] = User(name, password)

    def save_users(self):
        with open("data/users.pickle", "wb") as f:
            pickle.dump(self.users, f, protocol=pickle.HIGHEST_PROTOCOL)


class Program:
    def __init__(self):
        self.current_menu = None
        self.current_user: User = None
        self.options = ["login", "register"]
        self.user_manager = UserManager()

    def start(self):
        self.show_options()

    def show_options(self):
        self.current_menu = "main"
        option_str = "OPTIONS:\n------------\n"
        num = 1
        for option in self.options:
            option_str += f"{num} | {option}\n"
            num += 1
        choice = int(input(f"{option_str}\nChoice: "))
        if self.options[choice - 1] == "login":
            self.login()
        if self.options[choice - 1] == "register":
            self.register()

    def register(self):
        self.current_menu = "register"
        print("-----------")
        username = input("Create Username: ").lower()
        password = input("Create Password: ")
        self.user_manager.new_user(username, password)
        print(f"\n\nCreated new user: {username.upper()}\n\n")
        self.user_manager.save_users()
        self.show_options()

    def login(self):
        self.current_menu = "login"
        print("-----------")
        username = input("Username: ").lower()
        password = input("Password: ")
        if username in self.user_manager.users:
            if self.user_manager.users[username].password == password:
                self.current_user = self.user_manager.users[username]
                print(f"Logged in as {username.upper()}")
                self.current_menu = "hub"
                self.logged()
                return
        print("\n\nINCORRECT password or username\n\n")
        self.show_options()

    def logged(self):
        self.current_menu = "logged in"


program = Program()
program.start()
